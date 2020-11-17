import os
from subprocess import call
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM


class Runner(object):

    def main(self):
        PORT_NUMBER = 8000
        SIZE = 1024

        hostName = "app"
        SERVER_IP   = '0.0.0.0'
        mySocket = socket( AF_INET, SOCK_STREAM )
        mySocket.bind( (SERVER_IP, 8050) ) # Bind to port 8080
        mySocket.listen(5)  # listen for connections

        while True:
            (t1, t2) = mySocket.accept() # accept the connection
            # recieve the data from t1 which is the socket sending to us
            data = t1.recv(SIZE)
            print("test")
            os.system("xterm retext")

if __name__ == "__main__":
    r = Runner()
    r.main()
