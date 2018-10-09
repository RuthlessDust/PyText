from tkinter import Tk, Label, Button

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title = ("PyText: Main Menu")
        self.label = Label(master, text="Main Menu")
        self.label.pack()

root = Tk()
menu = MainMenu(root)
root.mainloop()