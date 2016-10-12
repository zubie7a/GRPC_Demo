from __future__ import print_function
import grpc
import time
import services_pb2 as pb
from sense_hat import SenseHat


def run():
    # The address of the GRPC Server.
    address = "52.34.52.17:50001"
    # Create a connection to that address.
    connection = grpc.insecure_channel(address)
    # Create a GRPC Client from that connection.
    client = pb.RegisterServiceStub(connection)
    # Instantiate the message struct that the RPC takes.
    message = pb.StatusRequest()
    while True:
        # Make a RPC call to the server with that message.
        response = client.GetStatus(message)
        # Print the server's response
        counter = response.appData.counter
        msg = "Attendants {} :-)".format(counter)
        print(msg)
        sense = SenseHat()
        sense.show_message(msg, text_colour=[255, 0, 0])

        X = [255, 255, 255]  # White
        O = [0, 0, 0]  # Black
        A = [42, 42, 42] # Gray
        gopher_face = [
        A, A, A, A, A, A, A, A,
        A, X, O, A, A, X, O, A,
        A, X, X, A, A, X, X, A,
        A, A, A, A, A, A, A, A,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        ]
        sense.set_pixels(gopher_face)
        time.sleep(3)

if __name__ == '__main__':
  run()