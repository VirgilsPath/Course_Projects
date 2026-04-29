### DATA PLAYGROUND - DO NOT DELETE THESE VARIABLES ###

# Dataset 1: Simple Lists
list_a = [12, 45, 67, 23, 89, 12, 90, 5, 23]
list_b = [23, 90, 11, 5, 78, 12, 40]

# Dataset 2: List of Strings
text_data = ["data", "python", "sql", "data", "excel", "python", "data", "tableau", "sql"]

# Dataset 3: List of Dictionaries (Employees)
staff = [
    {"name": "Jordan", "salary": 55000, "dept": "Sales"},
    {"name": "Taylor", "salary": 48000, "dept": "Admin"},
    {"name": "Alex", "salary": 72000, "dept": "Tech"},
    {"name": "Morgan", "salary": 61000, "dept": "Sales"},
    {"name": "Riley", "salary": 42000, "dept": "Admin"},
    {"name": "Casey", "salary": 85000, "dept": "Tech"}
]

# Dataset 4: Dictionary Mapping (Company IDs to Names)
companies_map = {
    101: "TechFlow",
    102: "GreenGrid",
    103: "BlueWave",
    104: "SkyNet"
}

# Dataset 5: List of Tuples (Company ID, Sent, Opened)
email_stats = [
    (101, 1000, 400),
    (102, 500, 100),
    (103, 2000, 1800),
    (104, 750, 50)
]

### YOUR CODE STARTS BELOW THIS LINE ###
# Challenge 1
new_list = list(set(list_a) & set(list_b))
new_list.sort(reverse=True)
print(new_list)

# Challenge 2
word_counter = {}

for i in text_data:
    if i in word_counter:
        word_counter[i] += 1
    else:
        word_counter[i] = 1
print(word_counter)

# Challenge 3
ballers = []

for row in staff:
    if row['salary'] > 50000:
        ballers.append(row['name'])
ballers.sort()
print(ballers)

# Challenge 4
for stats in email_stats:
    company_id = stats[0]
    sent = stats[1]
    opened = stats[2]

    name = companies_map[company_id]
    unopend = sent - opened

    print(f"{name} | {sent} | {unopend}")