import random
import json

crime_options = ["THEFT", "BATTERY", "CRIMINAL DAMAGE", "ASSAULT", "ROBBERY"]
loc_options = ["STREET", "SIDEWALK", "APARTMENT", "PARKING LOT"]

bigger_data = []

# This will build 100 fake crime dictionaries
for i in range(1, 101):
    bigger_data.append({
        "id": 1000 + i,
        "crime": random.choice(crime_options),
        "location": random.choice(loc_options),
        "district": random.choice([1, 2, 3, 4, 5]),
        "arrest": random.choice([True, False])
    })

print(f"Successfully loaded {len(bigger_data)} records!")

with open('data.json', 'w') as f:
    json.dump(bigger_data, f, indent=4)