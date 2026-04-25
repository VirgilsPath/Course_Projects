import csv
import random
from datetime import datetime, timedelta

# Built a CSV with 100 rows containing four columns
def generate_dirty_data(filename='dirty_finance_data.csv', num_rows=100):
    # Inconsistent categories with different casing and extra spaces
    categories = ['Food', 'food', 'FOOD ', ' Transport', 'Utilities', 'utilities', 'Entertainment', ' Entertainment']

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # Writing header
        writer.writerow(['transaction_id', 'amount', 'category', 'date'])

        start_date = datetime(2024, 1, 1)

        for i in range(1, num_rows + 1):
            # Column 1: Transaction ID (Standard integer)
            t_id = 1000 + i

            # Column 2: Amount (Injecting errors: missing or strings with symbols)
            error_type = random.random()
            if error_type < 0.1:        # 10% chance of a missing value (empty string)
                amount = ""
            elif error_type < 0.3:      # 20% chance of a string with symbols like "$" and ","
                raw_val = random.uniform(10, 5000)
                amount = f"${raw_val:,.2f}"
            else:                       # 70% chance of a clean float
                amount = round(random.uniform(10, 5000), 2)
            
            # Column 3: Category (Injecting inconsistent casing and leading/trailing spaces)
            category = random.choice(categories)

            # Column 4: Date (Injecting empty strings for missing data)
            if random.random() < 0.15:  # 15% chance of an empty date string
                date_str = ""
            else:
                random_days = random.randint(0, 365)
                date_obj = start_date + timedelta(days=random_days)
                date_str = date_obj.strftime("%Y-%m-%d")
            
            # Writing the row to the CSV file
            writer.writerow([t_id, amount, category, date_str])

# Run generator
generate_dirty_data()
print("Noice")