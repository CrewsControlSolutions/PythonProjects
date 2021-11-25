
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tblPersons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        colFName TEXT, \
        colLName TEXT, \
        colEmail TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tblPersons(colFName, colLName, colEmail) VALUES \
        (?,?,?)", ('Jerry','Anderson','janders@gmail.com'))
    cur.execute("INSERT INTO tblPersons(colFName, colLName, colEmail) VALUES \
        (?,?,?)", ('Tommy','Sam','tman@gmail.com'))
    cur.execute("INSERT INTO tblPersons(colFName, colLName, colEmail) VALUES \
        (?,?,?)", ('Crystal','Ricardo','diamondsforme47@gmail.com'))
    cur.execute("INSERT INTO tblPersons(colFName, colLName, colEmail) VALUES \
        (?,?,?)", ('Chris','Applewood','crockymate022@hotmail.com'))
    cur.execute("INSERT INTO tblPersons(colFName, colLName, colEmail) VALUES \
        (?,?,?)", ('Ryan','Campbell','racecardude@hotmail.com'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT colFName, colLName, colEmail FROM tblPersons \
        WHERE colFName = 'Jerry'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], \
                                                                item[1], \
                                                                item[2])
    print(msg)

















