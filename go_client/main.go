package main

import (
	"log"

	pb "protos"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

const (
	address = "52.34.52.17:50001"
)

func main() {
	// Set up a connection to the server.
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewSearchServiceClient(conn)

	// Contact the server and print out its response.
	r, err := c.Search(context.Background(), &pb.SearchRequest{Query: "Gopher DevOps"})
	if err != nil {
		log.Fatalf("Could not search: %v", err)
	}
	log.Printf("GRPC Response: %s", r.Reply)
}
