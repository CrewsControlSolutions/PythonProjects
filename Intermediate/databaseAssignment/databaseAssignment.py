## 
##Python: 3.10.0
## 
##Author: Kyle Crews
## 
##Purpose: Iterate through a list of text strings and
##store strings ending with '.txt' in a SQLite3
##database. Print those text strings to the console.
##

import sqlite3


##determine whether an element in a tuple ends with
##a specified sub-string. The tuple and sub-string must be
##passed to this function.
def findElements(stringList, subString):
    """Returns a tuple containing elements from the
    passed tuple stringList that end with the
    passed string subString."""
    # create an empty tuple for storing elements ending with the
    # sub string
    containsSubString = ()
    # find elements ending in the sub-string and store in a
    # tuple
    for item in stringList:
        if item.endswith(subString):
            containsSubString += (item,)
    # output the tuple containing elements of interest
    return containsSubString


# create database to store elements in passed tuple
def databaseStore(inputTuple):
    """Store elements of passed tuple inputTuple in a
    SQLite3 database called "elementsOfInterest"."""
    conn = sqlite3.connect('elementsOfInterest.db')

    # create table if not already made
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tblElements( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            colElement TEXT \
            )")
        conn.commit()

    # cycle through tuple to store each element in database
    for item in inputTuple:
        with conn:
            cur = conn.cursor()
            # note that the execute method for the cursor
            # requires that a tuple be passed for the optional
            # second parameter. note to self: do not forget
            # the comma that constitutes part of a tuple
            cur.execute("INSERT INTO tblElements(colElement) \
                VALUES (?)", (item,))
        conn.commit()
    conn.close()


# aesthetically display the elements of a tuple ending in the
# specified
# substring to the screen
def prettyPrint(inputTuple, subString):
    output = findElements(inputTuple, subString)
    for i in output:
        print(i)


# the provided tuple containing various file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
# the desired sub-string of interest
subString = '.txt'

# print the elements of the passed tuple matching the passed
# criteria
prettyPrint(fileList, subString)
# store in a database the elements from the tuple matching the
# desired criteria
databaseStore(findElements(fileList, subString))
