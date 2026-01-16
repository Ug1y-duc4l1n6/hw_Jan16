import sqlite3

conn = sqlite3.connect('teams.db')
cursor = conn.cursor()
query = """
    CREATE TABLE IF NOT EXISTS teams(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CITY TEXT,
        NAME TEXT
    )
"""

cursor.execute(query)
conn.commit()
conn.close()