#
# Python Ver:   3.10._
#
# Author:   Kyle M. Crews
#
# Purpose:  This is a student tracking application that uses the Tkinter GUI module. This file is used strictly for
# functions need by its parent Python file.
#
# Tested OS: This code was written and tested to work with Mac OSX.
#

import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox


def centerWindow(self, w, h):
    screenWidth = self.master.winfo_screenwidth()
    screenHeight = self.master.winfo_screenheight()
    x = int((screenWidth / 2) - (w / 2))
    y = int((screenHeight / 2) - (h / 2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def askQuit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        self.master.destroy()
        os._exit(0)


def createDB(self):
    conn = sqlite3.connect('DBStudents.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tblStudents( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    colFName TEXT, \
                    colLName TEXT, \
                    colFullName TEXT, \
                    colPhone TEXT, \
                    colEmail TEXT, \
                    colCurrentCourse TEXT \
                    );")
        conn.commit()
    conn.close()


def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('DBStudents.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT colFName, colLName, colPhone, colEmail, colCurrentCourse FROM tblStudents WHERE colFullName = (?)""",
            [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txtFName.delete(0, END)
            self.txtFName.insert(0, data[0])
            self.txtLName.delete(0, END)
            self.txtLName.insert(0, data[1])
            self.txtPhone.delete(0, END)
            self.txtPhone.insert(0, data[2])
            self.txtEmail.delete(0, END)
            self.txtEmail.insert(0, data[3])
            self.txtCurrentCourse.delete(0, END)
            self.txtCurrentCourse.insert(0, data[4])


def addToList(self):
    varFName = self.txtFName.get()
    varLName = self.txtLName.get()
    varFName = varFName.strip()
    varLName = varLName.strip()
    varFName = varFName.title()
    varLName = varLName.title()
    varFullName = ("{} {}".format(varFName, varLName))
    print("varFullName: {}".format(varFullName))
    varPhone = self.txtPhone.get().strip()
    varEmail = self.txtEmail.get().strip()
    varCurrentCourse = self.txtCurrentCourse.get().strip()
    if not "@" or not "." in varEmail:
        print("Invalid email format.")
    if (len(varFName) > 0) and (len(varLName) > 0) and (len(varPhone) > 0) and (len(varEmail) > 0):
        conn = sqlite3.connect('DBStudents.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT COUNT(colFullName) FROM tblStudents WHERE colFullName = '{}'""".format(varFullName))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute(
                    """INSERT INTO tblStudents (colFName, colLName, colFullName, colPhone, colEmail, 
                    colCurrentCourse) VALUES (?,?,?,?,?,?)""",
                    (varFName, varLName, varFullName, varPhone, varEmail, varCurrentCourse))
                self.lstList1.insert(END, varFullName)
                onClear(self)
            else:
                messagebox.showerror("Name Error",
                                     "'{}' already exists in the database. Please choose a different name.".format(
                                         varFullName))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error", "Please ensure that there is data in all four fields.")


def onDelete(self):
    varSelect = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('DBStudents.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tblStudents""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with ({}) \nwill be "
                                                                    "permanently deleted from the database. "
                                                                    "\n\nProceed with the deletion request?".format(varSelect))
            if confirm:
                conn = sqlite3.connect('DBStudents.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tblStudents WHERE colFullName = '{}'""".format(varSelect))
                    onDeleted(self)
                    conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "Please consider fixing.")
    conn.close()


def onDeleted(self):
    self.txtFName.delete(0, END)
    self.txtLName.delete(0, END)
    self.txtPhone.delete(0, END)
    self.txtEmail.delete(0, END)
    self.txtCurrentCourse.delete(0, END)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    self.txtFName.delete(0, END)
    self.txtLName.delete(0, END)
    self.txtPhone.delete(0, END)
    self.txtEmail.delete(0, END)


def onRefresh(self):
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('DBStudents.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tblStudents""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT colFullName FROM tblStudents""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0, str(item))
                i = i + 1
    conn.close()


if __name__ == "__main__":
    pass
