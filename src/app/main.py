"""
Script that runs gui.
"""
import os
import tkinter as tk
from socket import socket, AF_INET, SOCK_STREAM

SERVER_IP   = '0.0.0.0'
PORT_NUMBER = 5000
SIZE = 1024


class ButtonMapper(object):

    @staticmethod
    def git():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('git', 8090))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def rstudio():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('rstudio', 8085))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def spyder():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('spyder', 7085))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def markdown():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('markdown', 8050))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def ibmsas():
        tempstr = " "
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('ibmsas', 7066))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def atom():
        # send to atom
        tempstr = "xterm firefox atom:7070"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('atom', 7070))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def jnotebook():
        tempstr = "xterm firefox atom:7070"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('jupyter', 7030))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def orange():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('orange', 7075))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def aphadoop():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('hadoopwrapper', 7090))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def apspark():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('spark', 8080))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def tableau():
        tempstr = " "
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('tableau', 7065))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def sqube():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('sonar-scanner', 8045))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def tflow():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('tensorflow', 7080))
        print("connected")
        mySocket.send(tmpstr.encode())

    @staticmethod
    def markdown():
        tmpstr = "hello"
        mySocket = socket( AF_INET, SOCK_STREAM )
        #mySocket.bind((SERVER_IP, 8000))
        mySocket.connect(('markdown', 8050))
        print("connected")
        mySocket.send(tmpstr.encode())


class MainGUI(object):

    def __init__(self):
        pass

    def create_window(self):
        self.root = tk.Tk()
        self.root.title("Application Selector")
        self.root.geometry("1000x750")

    def add_labels(self):
        instructions = tk.Text(self.root, height=5, width=52)
        instrtext = "Click the button of the application you would like to" + \
            " run"
        instructions.pack(side="top")
        instructions.insert(tk.END, instrtext)

    def add_buttons(self):

        btn = tk.Button(self.root, text="Rstudio",
            bd='5', command=ButtonMapper.rstudio)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Spyder",
            bd='5', command=ButtonMapper.spyder)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="IBM SAS",
            bd='5', command=ButtonMapper.ibmsas)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Git",
            bd='5', command=ButtonMapper.git)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Jupyter Notebook",
            bd='5', command=ButtonMapper.jnotebook)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Orange",
            bd='5', command=ButtonMapper.orange)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Atom IDE",
            bd='5', command=ButtonMapper.atom)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Apache Hadoop",
            bd='5', command=ButtonMapper.aphadoop)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Apache Spark",
            bd='5', command=ButtonMapper.apspark)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Tableau",
            bd='5', command=ButtonMapper.tableau)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Sonar Qube and Binaries",
            bd='5', command=ButtonMapper.sqube)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Tensorflow",
            bd='5', command=ButtonMapper.tflow)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Markdown",
            bd='5', command=ButtonMapper.markdown)
        btn.pack(side="top")


    def display(self):
        self.root.mainloop()


class Main(object):

    def run_app(self):
        mgui = MainGUI()
        mgui.create_window()
        mgui.add_labels()
        mgui.add_buttons()
        mgui.display()


if __name__ == "__main__":
    main = Main()
    main.run_app()
