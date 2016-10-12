package main

import (
	"log"
	pb "protos"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

func main() {
	// The address of the GRPC Server.
	address := "52.34.52.17:50001"
	// Create a connection to that address..
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	// Create a GRPC Client from that connection.
	client := pb.NewSearchServiceClient(conn)
	// Instantiate the message struct that the RPC takes.
	message := &pb.SearchRequest{Query: "Gopher DevOps"}
	// Make a RPC call to the server with that message.
	r, err := client.Search(context.Background(), message)
	if err != nil {
		log.Fatalf("Could not search: %v", err)
	}
	// Print the server's response.
	log.Printf("GRPC Response: %s", r.Reply)
}
