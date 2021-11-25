import os

full = '/Users/mikecrews/Documents/TechAcademy/Course/test.txt'

with open(full, 'r') as f:
    data = f.read()
    print(data)
    f.close()