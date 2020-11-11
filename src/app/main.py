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
        mySocket.connect(('git', 8080))
        print("connected")
        mySocket.send(tmpstr.encode())
        os.system("gnome-terminal -x sh")

    @staticmethod
    def rstudio():
        pass

    @staticmethod
    def spyder():
        pass

    @staticmethod
    def markdown():
        # run script by os
        # or just os.system("./notepad_pp.sh")
        pass


class MainGUI(object):

    def __init__(self):
        pass

    def create_window(self):
        self.root = tk.Tk()
        self.root.title("Application Selector")
        self.root.geometry("800x550")

    def add_labels(self):
        instructions = tk.Text(self.root, height=5, width=52)
        instrtext = "Click the button of the application you would like to" + \
            " run"
        instructions.pack(side="top")
        instructions.insert(tk.END, instrtext)

    def add_buttons(self):

        btn = tk.Button(self.root, text="Rstudio",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Spyder",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="IBM SAS",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Git",
            bd='5', command=ButtonMapper.git)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Jupyter Notebook",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Orange",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Visual Studio Code IDE",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Apache Hadoop",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Apache Spark",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Tableu",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Sonar Qube and Binaries",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Tensorflow",
            bd='5', command=None)
        btn.pack(side="top")

        btn = tk.Button(self.root, text="Markdown",
            bd='5', command=None)
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
