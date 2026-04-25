import csv

def clean_amount(raw_amount):
    if raw_amount == "":
        return 0.0
    if isinstance(raw_amount, str):
        clean_value = raw_amount.replace("$", "").replace(",", "")
        return float(clean_value)
    
    return float(raw_amount)

def clean_category(raw_category):
    clean_value = raw_category.strip().lower()
    return clean_value

"""print(clean_amount("$1,200.50"))
print(clean_amount(""))
print(clean_category(" Transport"))"""


# Empty list for clean data
all_cleaned_data = []

with open('dirty_finance_data.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        fixed_amt = clean_amount(row['amount'])
        fixed_cat = clean_category(row['category'])

        date = row['date'] if row['date'] != "" else "2024-01-01"
        
        clean_row = {
            'transaction_id': row['transaction_id'],
            'amount': fixed_amt,
            'category': fixed_cat,
            'date': date
        }
        all_cleaned_data.append(clean_row)

"""print(all_cleaned_data)"""

headers = ['transaction_id', 'amount', 'category', 'date']

with open('clean_finance_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)

    writer.writeheader()

    writer.writerows(all_cleaned_data)