import sqlite3

firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')
age = int(input('Enter your age: '))
personData = (firstName, lastName, age)

with sqlite3.connect('testDB.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
    # c.execute("UPDATE People SET LastName=? WHERE FirstName=? AND Age=?",
    #           ("O\'Connor", 'John', 11))

    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 50")
    # for row in c.fetchall():
    #     print(row)
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)