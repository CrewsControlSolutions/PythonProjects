import os


fName = 'test.txt'
fPath = '/Users/mikecrews/Documents/TechAcademy/Course/'


abPath = os.path.join(fPath, fName)
print(abPath)

with open(abPath, 'r') as f:
    data = f.read()
    print(data)
    f.close()