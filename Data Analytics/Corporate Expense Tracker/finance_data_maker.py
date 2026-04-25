import random
import json
import datetime

departments = []
transactions = []

dept_names = ['Sales', 'Engineering', 'Marketing', 'HR', 'Finance']

start_date = datetime.date(2026, 1, 1)
end_date = datetime.date.today()

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for i in range(len(dept_names)):
    departments.append({
        'dept_id': i + 1,
        'dept_name': dept_names[i],
        'budget': random.randint(50000, 100000)
    })

for i in range(1, 201):
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
    transactions.append({
        'trans_id': 1000 + i,
        'dept_id': random.choice([1, 2, 3, 4, 5]),
        'category': random.choice(['Software', 'Travel', 'Office Supplies', 'Hardware', 'Entertainment']),
        'amount': round(random.uniform(10.50, 5000.00), 2),
        'date': str(random_date)
    })

with open('departments.json', 'w') as f:
    json.dump(departments, f, indent=4)

with open('expenses.json', 'w') as f:
    json.dump(transactions, f, indent=4)