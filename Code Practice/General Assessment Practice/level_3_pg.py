from datetime import datetime

### BIGGER DATA PLAYGROUND ###

# Employee Directory (Department & Hire Date)
employees = {
    "emp_01": {"name": "Alex", "dept": "Tech", "hired": "2021-05-10"},
    "emp_02": {"name": "Jordan", "dept": "Sales", "hired": "2023-01-15"},
    "emp_03": {"name": "Taylor", "dept": "Tech", "hired": "2020-11-20"},
    "emp_04": {"name": "Morgan", "dept": "HR", "hired": "2022-03-05"},
    "emp_05": {"name": "Riley", "dept": "Sales", "hired": "2022-08-12"}
}

# Daily Sales Records
# Format: (Employee_ID, Amount, "YYYY-MM-DD")
sales_records = [
    ("emp_01", 1200.50, "2024-04-01"),
    ("emp_02", 800.00, "2024-04-01"),
    ("emp_01", 300.25, "2024-04-02"),
    ("emp_05", 1500.00, "2024-04-02"),
    ("emp_02", 450.75, "2024-04-03"),
    ("emp_03", 2000.00, "2024-04-03"),
    ("emp_06", 500.00, "2024-04-03") # Note: This ID isn't in the directory!
]

### YOUR CODE BELOW ###
# Challenge 1
total_sales = {}
for row in sales_records:
    try:
        emp_id = row[0]
        amount = row[1]
        date = row[2]
        dept = employees[emp_id]['dept']
        if dept in total_sales:
            total_sales[dept] += amount
        else:
            total_sales[dept] = amount
    except ValueError:
        print(f"Skipping {row}.")
        continue
    except KeyError:
        print(f"Skipping {row}. Employee {emp_id} not found.")
        continue
print(total_sales)

# Challenge 2
tech_employ_2021 = []
for row in employees.values():
    try:
        year = int(row['hired'][:4])
        if row['dept'] == 'Tech' and year < 2022:
            tech_employ_2021.append([row['name'], row['dept'], year])
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {row}.")
        continue
print(tech_employ_2021)

# Challenge 3
# Keys are departments, Values are the name of the person who made large sale
top_performers = {}
max_amounts = {}
for emp_id, amount, date in sales_records:
    try:
        person = employees[emp_id]
        dept = person['dept']
        name = person['name']
        if amount > max_amounts.get(dept, 0):
            max_amounts[dept] = amount
            top_performers[dept] = name
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {row}")
        continue
print(top_performers)

# Challenge 4
total_recent_sales = 0
target_date = "2024-04-02"

for emp_id, amount, date in sales_records:
    # Direct string comparison works because of the YYYY-MM-DD format
    if date >= target_date:
        total_recent_sales += amount

print(f"Total sales from {target_date} onwards: ${total_recent_sales}")