### WAREHOUSE DATA ###

# A list of every single item scanned coming off a truck
# We need to know: How many TIMES was each item scanned? (Word Count)
scanned_items = [
    "drill", "saw", "hammer", "drill", "drill", 
    "saw", "wrench", "hammer", "drill", "wrench"
]

# A list of sales transactions
# Format: (Item_Name, Quantity_Sold, Price_Per_Unit)
# We need to know: What is the total REVENUE for each item? (Summing Totals)
sales_data = [
    ("drill", 2, 100),
    ("saw", 1, 50),
    ("drill", 1, 100),
    ("wrench", 5, 20),
    ("hammer", 2, 15),
    ("wrench", 2, 20)
]

### YOUR CODE BELOW ###
# Challenge 1
inventory_count = {}
for item in scanned_items:
    if item in inventory_count:
        inventory_count[item] += 1
    else:
        inventory_count[item] = 1
print(inventory_count)

# Challenge 2
item_revenue = {}
for item_name, quantity_sold, price_per_unit in sales_data:
    try:
        total_revenue = (quantity_sold * price_per_unit)
        if item_name in item_revenue:
            item_revenue[item_name] += total_revenue
        else:
            item_revenue[item_name] = total_revenue
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {item_name, quantity_sold, price_per_unit}")
print(item_revenue)

# Challenge 3
for item, count in inventory_count.items():
    revenue = item_revenue.get(item, 0)
    print(f"{item} was scanned {count} times and made ${revenue:.2f} in revenue.")
