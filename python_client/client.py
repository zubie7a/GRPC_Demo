from __future__ import print_function
import grpc
import services_pb2 as pb

def run():
  # The address of the GRPC Server.
  address = "52.34.52.17:50001"
  # Create a connection to that address.
  connection = grpc.insecure_channel(address)
  # Create a GRPC Client from that connection.
  client = pb.RegisterServiceStub(connection)
  # Instantiate the message struct that the RPC takes.
  message = pb.CodeRequest()
  # Make a RPC call to the server with that message.
  response = client.GetCode(message)
  # Print the server's response
  print("GRPC Response: " + response.code)

if __name__ == '__main__':
  run()
  


