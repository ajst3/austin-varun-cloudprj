"""
Script that runs gui.
"""
import tkinter as tk

class MainGUI(object):

    def __init__(self):
        pass

    def create_window(self):
        self.root = tk.Tk()
        self.root.title("Application Selector")
        self.root.geometry("800x500")

    def add_labels(self):
        instructions = tk.Text(self.root, height=5, width=52)
        instrtext = "Click the button of the application you would like to" + \
            " run"
        instructions.pack(side="top")
        instructions.insert(tk.END, instrtext)

    def add_buttons(self):
        ntpd = tk.Button(self.root, text="Notepad++",
            bd='5', command=None)
        ntpd.pack(side="top")

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
