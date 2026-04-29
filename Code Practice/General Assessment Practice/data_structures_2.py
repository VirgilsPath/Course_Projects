### DATA STRUCTURES CHALLENGE: RETAIL ANALYTICS ###

# 1. Sales Transactions (List of Strings)
# Format: "StoreID | ProductID | Quantity"
raw_sales = [
    "S-101 | P-50 | 2",
    "S-102 | P-50 | 1",
    "S-101 | P-75 | 10",
    "S-103 | P-99 | 5",
    "S-101 | P-50 | 3",
    "S-102 | P-75 | 2",
    "S-103 | P-50 | invalid", # Bad data trap
]

# 2. Product Price List (Dictionary)
# Mapping ProductID -> Price
prices = {
    "P-50": 100.0,
    "P-75": 50.0,
    "P-99": 200.0
}

# 3. Store Location Map (Dictionary)
# Mapping StoreID -> City
stores = {
    "S-101": "New York",
    "S-102": "London",
    "S-103": "Tokyo"
}

### YOUR CODE BELOW ###
"""Task 1
The Clean Loop (List to Dictionary):
Create a dictionary called store_revenue. Loop through raw_sales and calculate the total revenue (Quantity * Price) for each store.

    Requirement: Use try/except to handle the "invalid" quantity.
    Requirement: You must look up the price in the prices dictionary using the ProductID."""

store_revenue = {}
for raw in raw_sales:
    try:
        parts = [p.strip() for p in raw.split("|")]
        store_id, product_id, quantity_str = parts
        try:
            quantity = int(quantity_str)
        except ValueError:
            quantity = 0
        price = prices[product_id]
        total = quantity * price
        store_revenue[store_id] = store_revenue.get(store_id, 0) + total

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw}.")
        continue
print(store_revenue)

"""Task 2
The Unique Product Check (Sets):
Create a Set called products_sold that contains every unique -
ProductID that appears in the raw_sales logs."""

products_sold = set()
for raw in raw_sales:
    try:
        parts = [p.strip() for p in raw.split("|")]
        store_id, product_id, quantity_str = parts
        products_sold.add(product_id)

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw}.")
        continue
print(products_sold)

"""Task 3
The City Report (Join):
Create a List of Tuples formatted as (City, Total_Revenue).

Hint: Use your store_revenue totals and "join" them with the stores dictionary to get the city names."""

city_rev = []
for store_id, total in store_revenue.items():
    try:
        city = stores[store_id]
        city_rev.append((city, total))

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {store_id}.")
        continue
print(city_rev)

"""Task 4
The Ranking (Sort):
Sort your list of tuples by Revenue in descending order."""

sorted_final1 = sorted(city_rev, key=lambda x: x[1], reverse=True)
print(sorted_final1)

# If cities were tied and not alphabetically sorted
sorted_final2 = sorted(city_rev, key=lambda x: (-x[1], x[0]))
print(sorted_final2)