import sqlite3
import json
import matplotlib.pyplot as plt

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE departments (
        dept_id INTEGER,
        dept_name TEXT,
        budget REAL
    )
''')

cursor.execute('''
    CREATE TABLE expenses (
        trans_id INTEGER,
        dept_id INTEGER,
        category TEXT,
        amount REAL,
        date TEXT
    )
''')

with open('departments.json', 'r') as f:
    data1 = json.load(f)

for row in data1:
    cursor.execute('''
        INSERT INTO departments (dept_id, dept_name, budget)
        VALUES (?, ?, ?)
    ''', (row['dept_id'], row['dept_name'], row['budget']))

with open('expenses.json', 'r') as f:
    data2 = json.load(f)

for row in data2:
    cursor.execute('''
        INSERT INTO expenses (trans_id, dept_id, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['trans_id'], row['dept_id'], row['category'], row['amount'], row['date']))

connection.commit()
print("Finance data loaded successfully!")

# Challenge 1
query1 = """
SELECT
    departments.dept_name,
    expenses.amount
FROM expenses
JOIN departments ON expenses.dept_id = departments.dept_id;
"""

cursor.execute(query1)
results1 = cursor.fetchall()

# Grab the column names from the cursor metadata
"""column_names = [description[0] for description in cursor.description]
print(column_names)

for row in results1:
    print(row)"""

# Challenge 2
query2 = """
SELECT
    departments.dept_name,
    expenses.category,
    expenses.amount
FROM expenses
JOIN departments ON expenses.dept_id = departments.dept_id
WHERE expenses.amount > 4000;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

# Grab the column names from the cursor metadata
"""column_names = [description[0] for description in cursor.description]
print(column_names)

for row in results2:
    print(row)"""

# Challenge 3
query3 = """
SELECT
    departments.dept_name,
    ROUND(SUM(expenses.amount), 2)
FROM expenses
JOIN departments ON expenses.dept_id = departments.dept_id
GROUP BY departments.dept_name
ORDER BY ROUND(SUM(expenses.amount), 2) DESC;
"""

cursor.execute(query3)
results3 = cursor.fetchall()

# Grab the column names from the cursor metadata
"""column_names = [description[0] for description in cursor.description]
print(column_names)

for row in results3:
    print(row)"""

# Challenge 4
query4 = """
SELECT
    departments.dept_name,
    ROUND(SUM(expenses.amount), 2),
    departments.budget,
    ROUND(departments.budget - SUM(expenses.amount), 2) AS Remaining
FROM expenses
JOIN departments ON expenses.dept_id = departments.dept_id
GROUP BY departments.dept_name
ORDER BY SUM(expenses.amount) DESC;
"""

cursor.execute(query4)
results4 = cursor.fetchall()

# Grab the column names from the cursor metadata
"""column_names = [description[0] for description in cursor.description]
print(column_names)

for row in results4:
    print(row)"""

# Challenge 5
query5 = """
SELECT
    departments.dept_name,
    ROUND(SUM(expenses.amount), 2),
    departments.budget,
    ROUND(departments.budget - SUM(expenses.amount), 2) AS Remaining
FROM expenses
JOIN departments ON expenses.dept_id = departments.dept_id
GROUP BY departments.dept_name
HAVING Remaining < -40000
ORDER BY SUM(expenses.amount) DESC;
"""

cursor.execute(query5)
results5 = cursor.fetchall()

# Grab the column names from the cursor metadata
"""column_names = [description[0] for description in cursor.description]
print(column_names)

for row in results5:
    print(row)"""

# Create two empty lists
names = []
balances = []

# Challenge 'for' loop to go through 'results5' and append
for row in results5:
    names.append(row[0])    # department name
    balances.append(row[3]) # remaining balance

# Build and customize the chart
plt.figure(figsize=(10, 6))
plt.bar(names, balances, color='crimson')

# Adding labels so people know what they are looking at
plt.title("Financial Risk Report: Departments Over $40k Deficit")
plt.xlabel("Department Name")
plt.ylabel("Remaining Budget ($)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save and Show the results
plt.tight_layout()
plt.savefig('deficit_chart.png')
print("Project Completed: Chart saved as 'deficit_chart.png'")
plt.show()