package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net"
	"net/http"
	"os"
	"path"
	"time"

	pb "protos"

	"github.com/gin-gonic/gin"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

// The application data keeps track of the amount of people that's actually registered, and the attendants.
// Simply retrieving the length of the attendants map is no good since when every attendant is given a
// registration code, and the code is immediately inserted into the map with a placeholder value, so that
// when the attendant register themselves, this code acts as some sort of confirmation, and also preventing
// code reuse.
// A global structure to maintain app data, please don't do this, its hackish,
// better to use storage :-) The good thing about using a proto defined struct
// is that this data can be sent via GRPC to a client or whatever and it will
// maintain its nice structure.
var appData *pb.AppData

// GetCode generates a one-time use code, which will be given to an attendant
// and which is needed for successfully registering. It is a random 32bit int,
// and its temporarily stored in the Attendants list with no name associated to
// it, so that when an attendant uses the code, first the code must be there,
// and second it must not have a name associated to it.
func (s *server) GetCode(ctx context.Context,
	in *pb.CodeRequest) (*pb.CodeResponse, error) {
	var code string
	for {
		// Generate a code until there's no other attendant with this code,
		// or it isn't already in the "database", since the code will be
		// the unique identifier for an attendant in the application logic
		// (not attendant name itself).
		code = fmt.Sprintf("%d", rand.Int31n(1<<31-1))
		if _, ok := appData.Attendants[code]; !ok {
			appData.Attendants[code] = ""
			break
		}
	}
	fmt.Printf("Requesting new code, result is: %v\n", code)
	return &pb.CodeResponse{Code: code}, nil
}

// server is used to implement the services outlined in the services proto.
type server struct{}

// GetStatus retrieves the application status via GRPC for whatever purpose, in
// our case it will be called on the RaspberryPi so that the SenseHat can
// a visual counter of attendants and many more things about the status :-)
func (s *server) GetStatus(ctx context.Context,
	in *pb.StatusRequest) (*pb.StatusResponse, error) {
	return &pb.StatusResponse{AppData: appData}, nil
}

// Basic function for serving the index template on a "/" GET request, binded
// at main runtime.
func serveHomepage(c *gin.Context) {
	c.HTML(http.StatusOK, "index.tmpl.html", appData)
}

// Function for registering an attentant, on the "/register" POST request,
// binded at main runtime.
func registerAttendant(c *gin.Context) {
	// Parse the request body (c.Request has standard type *http.Request).
	c.Request.ParseForm()
	// Incoming request has all the data in a JSON inside the "data" field.
	jsonString := c.Request.Form["data"][0]
	// Instantiate an attendant struct from the proto spec.
	attendant := &pb.Attendant{}
	// Decode the JSON string into the attendant struct.
	if err := json.Unmarshal([]byte(jsonString), attendant); err != nil {
		fmt.Printf("%v\n", err)
	}
	// If any of the values comes empty. Don't validate this EVER in the front
	// end, because there's ways around that, unless you are doing it both in
	// frontend and backend to avoid load on the server, but always do it at
	// minimum in backend :-)
	if attendant.FirstName == "" || attendant.LastName == "" ||
		attendant.Code == "" {
		msg := "Please fill all fields."
		c.JSON(http.StatusOK, msg)
		return
	}
	// If there's already an entry for that code in the attendants list.
	if name, ok := appData.Attendants[attendant.Code]; ok {
		// Check if the code has already been used, e.g. nothing is assigned
		// to it, an empty string, and the .
		if name == "" {
			// The entry for this code is the placeholder value, so register
			// this person's name associating it to that code.
			appData.Attendants[attendant.Code] =
				fmt.Sprintf("%v %v", attendant.FirstName, attendant.LastName)
			// Increase the attendant counter now that the code has been
			// successfully used to register someone.
			appData.Counter++
			msg := fmt.Sprintf("Successfully registered user with code %v",
				attendant.Code)
			fmt.Println(msg)
		} else {
			// There's already a name associated to this code, return that the
			// code has already been used.
			msg := fmt.Sprintf("The code %v has already been used.",
				attendant.Code)
			fmt.Println(msg)
			c.JSON(http.StatusOK, msg)
			return
		}
	} else {
		// This is not a code that has been previously generated.
		msg := fmt.Sprintf("The code %v is not a valid code.", attendant.Code)
		fmt.Println(msg)
		c.JSON(http.StatusOK, msg)
		return
	}
}

// Initialize the "global" application data structure, on the main runtime.
func initializeAppData() *pb.AppData {
	return &pb.AppData{
		Counter:    0,
		Attendants: map[string]string{},
	}
}

func main() {
	// Initialize the struct that will hold the application data, which will
	// hold the Attendants' status and also be passed to the templates to fill
	// in the application web pages when making some GET/POST requests, or to
	// some remote clients (like our RaspPi) via GRPC.
	appData = initializeAppData()
	// Initialize the random seed with the nanoseconds since epoch. This will
	// be used to generate the attendants one-time codes.
	rand.Seed(time.Now().UnixNano())

	// Create a Gin Gonic router.
	router := gin.New()
	router.Use(gin.Logger())
	// This application supposed to be retrieved via
	//
	//    $ go get github.com/zubie7a/grpc-demo
	//
	// so please don't break it until I find a way to access the templates/ and
	// static/ folders relatively and not absolutely (relative works fine on my
	// computer but NOT AT ALL on AWS, so better to be safe than sorry and just
	// use absolute path everywhere).
	srcPath := path.Join(os.Getenv("GOPATH"), "src")
	// Load the templates/ files location using the absolute path.
	router.LoadHTMLGlob(path.Join(srcPath,
		"github.com/zubie7a/grpc-demo/templates/*.tmpl.html"))
	// Load the static/ files location using the absolute path.
	router.StaticFS("/static", http.Dir(path.Join(srcPath,
		"github.com/zubie7a/grpc-demo/static")))

	// Define a simple GET for serving the index template.
	router.GET("/", serveHomepage)
	// Define the POST via which attendants will register into the application,
	// using a web brower (though there can also be a way for registering via
	// GRPC).
	router.POST("/register", registerAttendant)

	// Port for the Web Server and the GRPC Server.
	webPort, grpcPort := ":8080", ":50001"
	// Listen on this port with TCP for the GRPC Server.
	lis, err := net.Listen("tcp", grpcPort)
	if err != nil {
		fmt.Printf("Failed to listen: %v\n", err)
	}
	// Create a new generic GRPC Server.
	s := grpc.NewServer()
	// Register the services defined in the proto to this GRPC server.
	pb.RegisterRegisterServiceServer(s, &server{})

	c := make(chan int)
	go func() {
		s.Serve(lis)
	}()
	go func() {
		router.Run(webPort)
	}()
	// Block here forever to prevent program from exiting after launching both
	// servers on separate goroutines.
	<-c
}
