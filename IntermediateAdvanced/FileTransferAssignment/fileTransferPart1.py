import shutil
import os

# set the location of the directory of the files to be transferred
source = '/Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/IntermediateAdvanced/FileTransferAssignment/FolderA/'

# set the destination path directory
destination = '/Users/mikecrews/Documents/TechAcademy/GitHub/PythonProjects/IntermediateAdvanced/FileTransferAssignment/FolderB/'
files = os.listdir(source)

for i in files:
    # move the files represented by 'i' to their new destination
    shutil.move(source + i, destination)





