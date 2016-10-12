from __future__ import print_function
import grpc
import helloworld_pb2

def run():
  # The address of the GRPC Server.
  address = '52.34.52.17:50001'
  # Create a connection to that address.
  channel = grpc.insecure_channel(address)
  # Create a GRPC client from that connection.
  client = helloworld_pb2.GreeterStub(channel)
  # Make a GRPC call to the server.
  response = client.SayHello(helloworld_pb2.HelloRequest(name='Medellin DevOps'))
  # Print the server's response
  print("GRPC Response: " + response.message)

if __name__ == '__main__':
  run()
  