#
# Python Ver:   3.10._
#
# Author:   Kyle M. Crews
#
# Purpose:  This is a student tracking application that uses the Tkinter GUI module. This file is used strictly for
# GUI attributes need by its parent Python file.
#
# Tested OS: This code was written and tested to work with Mac OSX.
#

from tkinter import *
import tkinter as tk

import studentTrackingAssignmentFunc


def loadGUI(self):
    self.lblFName = tk.Label(self.master, text='First Name:')
    self.lblFName.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lblLName = tk.Label(self.master, text='Last Name:')
    self.lblLName.grid(row=2, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lblPhone = tk.Label(self.master, text='Phone Number:')
    self.lblPhone.grid(row=4, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lblEmail = tk.Label(self.master, text='Email Address:')
    self.lblEmail.grid(row=6, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lblCurrentCourse = tk.Label(self.master, text='Current Course:')
    self.lblCurrentCourse.grid(row=8, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)
    self.lblLName = tk.Label(self.master, text='Information:')
    self.lblLName.grid(row=0, column=2, padx=(0, 0), pady=(10, 0), sticky=N + W)

    self.txtFName = tk.Entry(self.master, text='')
    self.txtFName.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txtLName = tk.Entry(self.master, text='')
    self.txtLName.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txtPhone = tk.Entry(self.master, text='')
    self.txtPhone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txtEmail = tk.Entry(self.master, text='')
    self.txtEmail.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)
    self.txtCurrentCourse = tk.Entry(self.master, text='')
    self.txtCurrentCourse.grid(row=9, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N + E + W)

    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: studentTrackingAssignmentFunc.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0, 0), pady=(0, 0), sticky=N + E + S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=N + E + S + W)

    self.btnAdd = tk.Button(self.master, width=12, height=2, text='Add',
                            command=lambda: studentTrackingAssignmentFunc.addToList(self))
    self.btnAdd.grid(row=10, column=0, padx=(25, 0), pady=(45, 10), sticky=W)
    self.btnDelete = tk.Button(self.master, width=12, height=2, text='Delete',
                               command=lambda: studentTrackingAssignmentFunc.onDelete(self))
    self.btnDelete.grid(row=10, column=2, padx=(15, 0), pady=(45, 10), sticky=W)
    self.btnClose = tk.Button(self.master, width=12, height=2, text='Close',
                              command=lambda: studentTrackingAssignmentFunc.askQuit(self))
    self.btnClose.grid(row=10, column=4, columnspan=1, padx=(15, 0), pady=(45, 10), sticky=E)

    studentTrackingAssignmentFunc.createDB(self)
    studentTrackingAssignmentFunc.onRefresh(self)


if __name__ == "__main__":
    pass
