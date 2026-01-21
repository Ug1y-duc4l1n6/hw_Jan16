import sqlite3
import pandas as pd

conn = sqlite3.connect('teams.db')
cursor = conn.cursor()
query = """
    SELECT *
    FROM teams;
"""

cursor.execute(query)
results = cursor.fetchall()
conn.close()

'''results_df = pd.DataFrame(results, columns = ['id','city','name'])
print(results_df['city'])'''

cities = []
character_list = []
teams = []
for result in results:
    cities.append(result[1])
    character_list.append(len(result[1]))


print(cities)
print(character_list)
