from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd


def callback():
    name = fd.askdirectory()
    print(name)
    # txtPath.insert(0, name)
    return name


class ParentWindow(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550, 230)
        self.master.maxsize(550, 230)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        filepath = '(You have no directory selected.)'

        # 1st column
        self.btnBrowse1 = tk.Button(self.master, width=12, height=2, text="Browse...", command=callback)
        self.btnBrowse1.grid(row=0, column=0, padx=(30, 30), pady=(50, 5), sticky=W)
        self.btnBrowse2 = tk.Button(self.master, width=12, height=2, text="Browse...")
        self.btnBrowse2.grid(row=1, column=0, padx=(30, 30), pady=(5, 5), sticky=W)
        self.btnCheck = tk.Button(self.master, width=12, height=4, text="Check for files...")
        self.btnCheck.grid(row=2, column=0, padx=(30, 30), pady=(5, 5), sticky=W)

        # 2nd, 3rd, and 4th columns
        self.txtPath = tk.Label(self.master, width=36, text=filepath)
        self.txtPath.grid(row=0, column=1, rowspan=2, columnspan=3, padx=(10, 10), pady=(5, 5), sticky=W)
        self.txtField2 = tk.Entry(self.master, width=36, text='')
        self.txtField2.grid(row=1, column=1, rowspan=1, columnspan=3, padx=(10, 10), pady=(5, 5), sticky=W)
        self.btnCheck = tk.Button(self.master, width=12, height=4, text="Close Program")
        self.btnCheck.grid(row=2, column=3, padx=(50, 10), pady=(5, 5), sticky=E)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
