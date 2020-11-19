import os
from subprocess import call
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM


class Runner(object):

    def main(self):
        SERVER_IP   = '0.0.0.0'
        mySocket = socket(AF_INET, SOCK_STREAM)
        mySocket.bind((SERVER_IP, 7030)) # Bind to port 8080
        mySocket.listen(5)  # listen for connections

        while True:
            (t1, t2) = mySocket.accept() # accept the connection
            # recieve the data from t1 which is the socket sending to us
            data = t1.recv(1024)
            print("test")
            os.system("xterm -e firefox jserver:8888")

if __name__ == "__main__":
    r = Runner()
    r.main()
