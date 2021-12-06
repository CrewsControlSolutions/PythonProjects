import shutil
import os, time
from datetime import datetime, date

# set the location of the directory of the files to be transferred
path = '/Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/IntermediateAdvanced/FileTransferAssignment/FolderA/'

# set the destination path directory
destination = '/Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/IntermediateAdvanced/FileTransferAssignment/FolderB/'
files = os.listdir(path)

# set the current date and time
currentDate = datetime.now()
cDateStr = str(currentDate)

# set the format to be used for date and time
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'

# declare an empty tuple for storing a list of the files that are moved
movedFiles = ()

# cycle through every file in the source directory to determine whether a file has been added or modified within the last 24 hours
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