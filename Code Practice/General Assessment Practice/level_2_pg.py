from collections import Counter

### NEW DATA PLAYGROUND ###

# Product Catalog (Lookup Table)
# Format -> ID: {"name": Name, "price": Price}
catalog = {
    10: {"name": "Laptop", "price": 1200},
    20: {"name": "Mouse", "price": 25},
    30: {"name": "Monitor", "price": 300},
    40: {"name": "Keyboard", "price": 50}
}

# Customer Orders
# Format -> (Order_ID, Product_ID, Quantity)
orders = [
    (101, 10, 1),
    (102, 20, 2),
    (103, 10, 2),
    (104, 40, 5),
    (105, 30, 1)
]

# Recent Searches (For frequency practice)
searches = ["Laptop", "Mouse", "Laptop", "Webcam", "Laptop", "Mouse", "Keyboard"]

### YOUR CODE BELOW ###
# Challenge 1
counts = Counter(searches)
print(counts)

# Challenge 2
"""for order_id, product_id, quantity in orders:"""

for order in orders:
    order_id = order[0]
    product_id = order[1]
    quantity = order[2]

    name = catalog[product_id]['name']
    price = catalog[product_id]['price']

    print(f"Order {order_id}: {name} - Total: ${quantity * price}")

# Challenge 3
big_orders = []

for order in orders:
    order_id = order[0]
    product_id = order[1]
    quantity = order[2]

    price = catalog[product_id]['price']
    total_cost = quantity * price

    if total_cost > 500:
        big_orders.append(order_id)

print(big_orders)

# Challenge 4
"""ordered = {order[1] for order in orders}"""

ordered = set()

for order in orders:
    order_id = order[0]
    product_id = order[1]
    quantity = order[2]

    ordered.add(product_id)

print(ordered)