"""
Project: Functional Transaction Analyzer
Author: Miguel Angel Hernandez/VirgilsPath
Description: 
    A data processing tool designed to analyze financial transactions 
    using Functional Programming (FP) paradigms. This project replaces 
    standard imperative loops with recursive functions and higher-order 
    logic to ensure data immutability.

Key Concepts:
    - Recursion (Base cases & Recursive steps)
    - Pure Functions (No side-effects)
    - Higher-Order Functions (filter, lambda)
    - JSON Data Management
"""

import json

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

all_data = load_data('transactions.json')

# Filter 'withdrawal'
withdrawals = list(filter(lambda t: t['type'] == 'withdrawal', all_data))

def recursive_sum(transactions_list):
    if len(transactions_list) == 0:
        return 0
    
    first_amount = transactions_list[0]['amount']

    remaining_items = transactions_list[1:]

    return first_amount + recursive_sum(remaining_items)

def sum_by_category(data, category):
    if len(data) == 0:
        return 0
    
    first_item = data[0]
    rest_of_list = data[1:]

    if first_item['category'] == category:
        return first_item['amount'] +  sum_by_category(rest_of_list, category)
    else:
        return sum_by_category(rest_of_list, category)

def count_category(data, category):
    if len(data) == 0:
        return 0
    
    # Use 1 if it matches, 0 if it doesn't
    match = 1 if data[0]['category'] == category else 0

    return match + count_category(data[1:], category)

def count_high_value(data, threshold):
    if len(data) == 0:
        return 0
    
    # Use 1 if it matches, 0 if it doesn't
    match = 1 if data[0]['amount'] >= threshold else 0

    return match + count_high_value(data[1:], threshold)

# Get all ids
def get_all_ids(data):
    if len(data) == 0:
        return []
    
    first_item_list = [data[0]['id']]
    return first_item_list + get_all_ids(data[1:])

# Get ids by category
def get_ids_by_category(data, category):
    if len(data) == 0:
        return []
    
    first_item = data[0]
    rest_of_data = data[1:]

    if first_item['category'] == category:
        return [first_item['id']] + get_ids_by_category(rest_of_data, category)
    else:
        return get_ids_by_category(rest_of_data, category)


# Total of 'withdrawal' type
withdrawal_total = recursive_sum(withdrawals)
print(f"Total spent: ${withdrawal_total:.2f}")

# Summing just 'Dining' category
dining_total = sum_by_category(all_data, 'Dining')
print(f"Total spent on Dining: ${dining_total:.2f}")

# Summing just 'Gas' category
gas_total = sum_by_category(all_data, 'Gas')
print(f"Total spent on Gas: ${gas_total:.2f}")

# 'Dining' count
dining_count = count_category(all_data, 'Dining')
print(f"Number of Dining trips: {dining_count}")

# Testing count_high_value()
threshold_100 = count_high_value(all_data, 100)
print(f"Number of transactions at and above $100: {threshold_100}")

# Get all ids
all_ids = get_all_ids(all_data)
print(f"All ids: {all_ids}")

# Get ids for certain category
grocergy_id = get_ids_by_category(all_data, 'Grocery')
print(f"IDs for 'Grocery' category: {grocergy_id}")