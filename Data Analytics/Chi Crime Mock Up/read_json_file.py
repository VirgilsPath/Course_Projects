from pathlib import Path
import json

def get_path():
    return Path(__file__).parent / 'data.json'

def load_data():
    path = get_path()

    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return "File not found."

def filter_by_condition(dataset, key, value):
    return [row for row in dataset if row.get(key) == value]

def count_frequencies(dataset, key):
    key_count = {}
    for row in dataset:
        value = row.get(key)
        
        if value is None:
            continue
        
        if value in key_count:
            key_count[value] += 1
        else:
            key_count[value] = 1
            
    return key_count

def arrest_rate(dataset, first_key, second_key):
    crime_count = 0
    arrest_count = 0
    
    for row in dataset:
        # Check if the key string is in the row
        if first_key in row:
            crime_count += 1
            
            # Check if the second key string is in the row
            if second_key in row:
                if row[second_key] == True:
                    arrest_count += 1
    
    if crime_count == 0:
        return 0.0

    perc = (arrest_count / crime_count) * 100
    return f"{perc:.2f}%"

def most_frequent_location(dataset, key):
    key_count = {}
    max_so_far = None

    for row in dataset:
        value = row[key]
        if value in key_count:
            key_count[value] += 1
        else:
            key_count[value] = 1
    
    for first_key, first_value in key_count.items():
        if max_so_far is None or first_value > max_so_far[1]:
            max_so_far = (first_key, first_value)
    
    return max_so_far

def most_safe_location(dataset, key):
    key_count = {}
    min_so_far = None

    for row in dataset:
        value = row[key]
        if value in key_count:
            key_count[value] += 1
        else:
            key_count[value] = 1
    
    for first_key, first_value in key_count.items():
        if min_so_far is None or first_value < min_so_far[1]:
            min_so_far = (first_key, first_value)
    
    return f"Safest District: {min_so_far[0]} | Crime: {min_so_far[1]}"