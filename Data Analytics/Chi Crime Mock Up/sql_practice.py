import sqlite3
import json

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE crimes (
        id INTEGER,
        crime TEXT,
        location TEXT,
        district INTEGER,
        arrest BOOLEAN
    )
''')

with open('data.json', 'r') as f:
    data = json.load(f)

for row in data:
    cursor.execute('''
        INSERT INTO crimes (id, crime, location, district, arrest)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['id'], row['crime'], row['location'], row['district'], row['arrest']))

connection.commit()
print("SQL Database created and loaded successfully!\n")



# Challenge 1
query1 = "SELECT * FROM crimes;"

cursor.execute(query1)
results1 = cursor.fetchall()
"""for row in results1:
    print(row)"""


# Challenge 2
query2 = "SELECT crime, district FROM crimes;"

cursor.execute(query2)
results2 = cursor.fetchall()
"""for row in results2:
    print(row)"""


# Challenge 3
query3 = "SELECT * FROM crimes WHERE district = 3;"

cursor.execute(query3)
results3 = cursor.fetchall()
"""for row in results3:
    print(row)"""

# Challenge 4
query4 = "SELECT * FROM crimes WHERE crime = 'THEFT'"

cursor.execute(query4)
results4 = cursor.fetchall()
"""for row in results4:
    print(row)"""

# Challenge 5
query5 = "SELECT COUNT(*) FROM crimes WHERE district = 3;"

cursor.execute(query5)
results5 = cursor.fetchall()
"""for row in results5:
    print(row)"""

# Challenge 6
query6 = "SELECT crime, COUNT(*) FROM crimes GROUP BY crime;"

cursor.execute(query6)
results6 = cursor.fetchall()
"""for row in results6:
    print(row)"""

# Challenge 7
query7 = "SELECT crime, COUNT(*) FROM crimes GROUP BY crime ORDER BY COUNT(*) DESC;"

cursor.execute(query7)
results7 = cursor.fetchall()
"""for row in results7:
    print(row)"""