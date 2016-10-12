package main

import (
	"fmt"
	"net"
	"net/http"
	"os"
	"path"
	"time"

	"golang.org/x/net/context"

	"google.golang.org/grpc"

	pb "protos"

	"github.com/gin-gonic/gin"
)

// A global counter that will be increased first with a timer and then via RPC calls.
var global int

// server is used to implement helloworld.GreeterServer.
type server struct{}

// SayHello implements helloworld.GreeterServer
func (s *server) Search(ctx context.Context, in *pb.SearchRequest) (*pb.SearchResponse, error) {
	fmt.Println("Incoming:", in.Query)
	res := fmt.Sprintf("Hello %s, the counter is at %d", in.Query, global)
	return &pb.SearchResponse{Reply: res}, nil
}

func main() {

	// Port for the Web Server.
	webPort := ":8080"
	// Create a Gin Gonic router.
	router := gin.New()
	router.Use(gin.Logger())
	// This is supposed to be retrieved via "go get github.com/zubie7a/grpc-demo" so please don't
	// break it until I find a way to access the templates/ and static/ folders relatively and
	// not absolutely (relative seems to work on my computer but NOT AT ALL on AWS).
	srcPath := path.Join(os.Getenv("GOPATH"), "src")
	// Load the templates using the absolute path.
	router.LoadHTMLGlob(path.Join(srcPath, "github.com/zubie7a/grpc-demo/templates/*.tmpl.html"))
	// Load the static files using the absolute path.
	router.StaticFS("/static", http.Dir(path.Join(srcPath, "github.com/zubie7a/grpc-demo/static")))
	// Define a simple GET for serving the index template.
	router.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.tmpl.html", nil)
	})

	// Port for the GRPC Server.
	grpcPort := ":50001"
	// Listen on this port with TCP.
	lis, err := net.Listen("tcp", grpcPort)
	if err != nil {
		fmt.Printf("Failed to listen: %v\n", err)
	}
	// Create a new generic GRPC server.
	s := grpc.NewServer()
	// Register the services defined in the proto to this GRPC server.
	pb.RegisterSearchServiceServer(s, &server{})

	c := make(chan int)
	go func() {
		for {
			time.Sleep(1 * time.Second)
			global++
		}
	}()
	go func() {
		s.Serve(lis)
	}()
	go func() {
		router.Run(webPort)
	}()
	// Block here forever to prevent program from exiting after launching both goroutines.
	<-c

}
