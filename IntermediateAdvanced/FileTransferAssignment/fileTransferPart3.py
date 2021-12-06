#
# Python Ver:   3.10.0
#
# Author:   Kyle C.
#
# Purpose:  Create a script with a UI that allows a user to transfer files from a user-defined originating directory to a user-defined ending directory. Only files that have been created or modified in the last 24 hours will be transferred.
#
# Tested OS: This code was written and tested to work with MacOSX.
#

from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import shutil
import os
from datetime import datetime


# function for the user to set the originating directory
def dirStart():
    source = fd.askdirectory()
    folderPathStart.set(source)
    print(source)
    return source


# function for the user to set the destination directory
def dirEnd():
    source = fd.askdirectory()
    folderPathEnd.set(source)
    print(source)
    return source


# check the originating directory for files modified or created in the last 24 hours and transfer any matching files
# to the destination directory
def initiateTransfer():
    # return an error if either the originating or destination directory are blank (not filled out)
    if folderPathStart.get() == '' or folderPathEnd.get() == '':
        print('Error: The originating and/or destination directory is not set.')
        return

    else:
        # set the location of the directory of the files to be transferred
        path = str(folderPathStart.get()+'/')

        # set the destination path directory
        destination = str(folderPathEnd.get()+'/')
        files = os.listdir(path)

        # set the current date and time
        currentDate = datetime.now()
        cDateStr = str(currentDate)

        # set the format to be used for date and time
        datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

        # declare an empty tuple for storing a list of the files that are moved
        movedFiles = ()

        # cycle through every file in the source directory to determine whether a file has been added or modified
        # within the last 24 hours
        for i in files:
            # determine the modification/creation date of a file
            lastModifiedDate = datetime.fromtimestamp(os.path.getmtime(path + i))
            lModDateStr = str(lastModifiedDate)

            # determine the difference in time between the current time and the file's modification/creation time
            diff = datetime.strptime(cDateStr, datetimeFormat) - datetime.strptime(lModDateStr, datetimeFormat)

            # move the file if the difference in time is less than 1 day (or 24 hours, to be exact)
            if diff.days < 1:
                tupI = (i,)
                shutil.move(path + i, destination)
                movedFiles = movedFiles + tupI

        # for added convenience for the user, print the files that were successfully moved, if any
        print("The following files, having been created or modified within the last 24 hours, have been moved to the home "
              "office: " + str(movedFiles))


class ParentWindow(Frame):

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(1300, 230)
        self.master.maxsize(1300, 230)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        # 1st column
        self.btnBrowse1 = tk.Button(self.master, width=30, height=2, text="Browse for Originating Directory...", command=dirStart)
        self.btnBrowse1.grid(row=0, column=0, padx=(30, 30), pady=(50, 5), sticky=W)
        self.btnBrowse2 = tk.Button(self.master, width=30, height=2, text="Browse for Destination Directory...", command=dirEnd)
        self.btnBrowse2.grid(row=1, column=0, padx=(30, 30), pady=(5, 5), sticky=W)
        self.btnCheck = tk.Button(self.master, width=12, height=4, text="...")
        self.btnCheck.grid(row=2, column=0, padx=(30, 30), pady=(5, 5), sticky=W)

        # 2nd, 3rd, and 4th columns
        self.txtPathStart = tk.Entry(self.master, width=100, text=folderPathStart)
        self.txtPathStart.grid(row=0, column=1, rowspan=2, columnspan=3, padx=(10, 10), pady=(5, 5), sticky=W)
        self.txtPathEnd = tk.Entry(self.master, width=100, text=folderPathEnd)
        self.txtPathEnd.grid(row=1, column=1, rowspan=1, columnspan=3, padx=(10, 10), pady=(5, 5), sticky=W)
        self.btnCheck = tk.Button(self.master, width=12, height=4, text="Check Files", command=initiateTransfer)
        self.btnCheck.grid(row=2, column=3, padx=(50, 10), pady=(5, 5), sticky=E)


if __name__ == "__main__":
    root = tk.Tk()
    # declare a string variable to be used for storing the originating directory
    folderPathStart = StringVar()
    # declare a string variable to be used for storing the destination directory
    folderPathEnd = StringVar()
    App = ParentWindow(root)
    root.mainloop()
