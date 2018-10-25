import tkinter
path_to_file = "/home/cmk/Desktop/Projects/PyText/PyText-experimental/test.txt"
file = open(path_to_file, "r+")
cont = file.read()

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title = ("PyText: {f}".format(f=path_to_file))
        text = tkinter.Text(master, height=29, width=60)
        text.insert(tkinter.END, cont)
        text.pack()
root = tkinter.Tk()
root.title("PyText: {f}".format(f=path_to_file))
menu = MainMenu(root)
root.mainloop()
