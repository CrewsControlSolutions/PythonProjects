#
# Python Ver:   3.10._
#
# Author:   Kyle M. Crews
#
# Purpose:  This is a student tracking application that uses the Tkinter GUI module. This file references two other
# Python files, one of which contains all functions and the other which contains all GUI attributes.
#
# Tested OS: This code was written and tested to work with Mac OSX.
#

from tkinter import *
import tkinter as tk

import studentTrackingAssignmentFunc
import studentTrackingAssignmentGUI


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550, 450)
        self.master.maxsize(550, 450)
        studentTrackingAssignmentFunc.centerWindow(self, 500, 300)
        self.master.title("The Tkinter Student Tracker--Big Brother is Watching")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: studentTrackingAssignmentFunc.askQuit(self))
        arg = self.master

        studentTrackingAssignmentGUI.loadGUI(self)

        # menubar = Menu(self.master)
        # filemenu = Menu(menubar, tearoff=0)
        # filemenu.a


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

















