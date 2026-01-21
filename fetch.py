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
cities_length = []
teams_length = []
for result in results:
    cities.append(result[1])
    cities_length.append(len(result[1]))
    teams_length.append(len(result[2]))

combined_tuple = list(zip(cities_length, teams_length))
print(cities)
print(cities_length)
print(teams_length)
print(combined_tuple)