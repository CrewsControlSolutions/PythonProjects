# 
# Python: 3.10.0
# 
# Author: Kyle Crews
# 
# Purpose: A demonstration a function that returns all .txt files and their associated "last modified" dates from within a user specified directory. The user must pass the full path of the directory.

import os, time, datetime

#returns all .txt files (along with their modification dates) from within the passed path directory
def listAllTxtFiles(dirPath):
    """Returns all .txt files and their associated "last modified" dates within a directory. User passes the directory's full path."""

    #list all contents of the passed directory and assign it to a variable 
    dirs = os.listdir(dirPath)
    
    #iterate through all files in directory
    for item in dirs:
        #check whether a file in the directory is a txt file
        if '.txt' in item:
            #determine the full file path
            abPath = os.path.join(dirPath, item)
            #determine the modification time of the file using the file's full file path
            modTime = os.path.getmtime(abPath)
            #determine only the date that the file was last modified
            userFriendlyTime = time.strftime('%m/%d/%Y', time.localtime(modTime))
            #print the file name and modified date to the screen
            print(item + ' last modified ' + userFriendlyTime)

#IMPORTANT: this is my directory path for my local machine. Developers should change this directory path to a desired directory relative to their machine.
dirPath = '/Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/Intermediate/scriptAssignment/folderOfSampleFiles/'
#call on the function that returns all txt files by passing the full directory path into the function
listAllTxtFiles(dirPath)