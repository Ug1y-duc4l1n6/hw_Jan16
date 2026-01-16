import sqlite3

conn = sqlite3.connect('teams.db')
cursor = conn.cursor()
query = """
    INSERT INTO teams(CITY,NAME)
    VALUES
    ('Buffalo','Bills'), 
    ('Denver','Broncos'),
    ('San Fransisco','49ers'),
    ('Seattle','Seahawks'),
    ('Houston','Texans'),
    ('New England', 'Patriots'),
    ('Los Angelos', 'Rams'),
    ('Chicago', 'Bears')
"""

cursor.execute(query)
conn.commit()
conn.close()