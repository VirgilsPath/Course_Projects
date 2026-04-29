### DATA PLAYGROUND ###

# Prices per unit
prices = {"widget": 5, "gadget": 10, "gizmo": 20}

# Messy logs of sales: "Product_Name:Quantity"
# Note: Some have weird capitalization!
raw_sales = ["Widget:5", "gadget:2", "GIZMO:1", "widget:10", "Gadget:4"]

### TASK ###
# 1. Create a dictionary called 'summary' that totals the QUANTITY for each product.
#    (Everything must be lowercase so 'Widget' and 'widget' count together).
# 2. Calculate the total REVENUE (Quantity * Price) for the whole list.

# Challenge 1
summary = {}

for raw in raw_sales:
    try:
        key, value = raw.lower().split(":")
        value = int(value)
        
        if key in summary:
            summary[key] += value
        else:
            summary[key] = value
    except ValueError:
        print(f"Skipping {raw}")
        continue

print(summary)

# Challenge 2

total_rev = 0

for product, quantity in summary.items():
    price = prices[product]
    total_rev += (quantity * price)

print(total_rev)