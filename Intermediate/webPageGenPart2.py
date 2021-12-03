#
# Python Ver:   3.10.0
#
# Author:   Kyle C.
#
# Purpose:  This is a web page generator that ingests text entered by the user and displays the text in the header of
# the webpage
#
# Tested OS: This code was written and tested to work with MacOSX.
#

from tkinter import *
import tkinter as tk
import webbrowser


# display the webpage containing the user's entered text
def displayWebContent(self):
    # grabs the text (if any) entered by the user in the field
    inputText = self.txtField.get()
    print(inputText)
    f = open('webpage.html', 'w')
    f.write('<html>'
            '<body>'
            '<h1>'
            + inputText +
            '</h1>'
            '</body>'
            '</html>')
    f.close()

    filename = 'file:////Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/Intermediate/' + 'webpage.html'
    webbrowser.open_new_tab(filename)


# utilize a Tkinter window frame for the user to type and submit their desired text
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(650, 100)
        self.master.maxsize(650, 100)
        self.master.title("Webpage Generator Part Two")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        # 1st column. utilizes a lambda function to get the latest input (if any) from the window
        self.btnGenerate = tk.Button(self.master, width=24, height=2, text="Generate Webpage With My Text", command=lambda: displayWebContent(self))
        self.btnGenerate.grid(row=0, column=0, padx=(30, 30), pady=(20, 5), sticky=W)

        # 2nd, 3rd, and 4th columns
        self.txtField = tk.Entry(self.master, width=36, text='')
        self.txtField.grid(row=0, column=1, rowspan=1, columnspan=3, padx=(10, 10), pady=(20, 5), sticky=W)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
