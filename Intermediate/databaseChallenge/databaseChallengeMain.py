import sqlite3

speciesData1 = ("Jean-Baptiste Zorg", "Human", 122)
speciesData2 = ("Korben Dallas", "Meat Popsicle", 100)
speciesData3 = ("Ak\'not", "Mangalore", -5)

conn = sqlite3.connect(':memory:')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tblRoster(colName TEXT, colSpecies TEXT, colIQ INT)")
    conn.commit()

    cur.execute("INSERT INTO tblRoster VALUES(?, ?, ?)", speciesData1)
    cur.execute("INSERT INTO tblRoster VALUES(?, ?, ?)", speciesData2)
    cur.execute("INSERT INTO tblRoster VALUES(?, ?, ?)", speciesData3)

    cur.execute("UPDATE tblRoster SET colSpecies=? WHERE colName=?", ("Human", "Korben Dallas"))

    cur.execute("SELECT colName, colIQ FROM tblRoster WHERE colSpecies = 'Human'")
    for row in cur.fetchall():
        print(row)
















