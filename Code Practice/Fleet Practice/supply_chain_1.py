### PROJECT: GLOBAL RETAIL SUPPLY CHAIN ###

# Dataset 1: Warehouse Shipments (The Messy Logs)
# Format: "ShipmentID | Product_Name | Quantity | Status | Destination"
shipment_logs = [
    "SH-001 | wireless mouse | 50 | Shipped | New York",
    "SH-002 | USB-C ADAPTER | 100 | pending | london",
    "SH-003 |  Mechanical Keyboard | invalid | Shipped | Tokyo ", # Bad Qty & extra spaces
    "SH-004 | n/a | 25 | PENDING | Berlin",                     # Missing Product Name
    "SH-005 | wireless mouse | NULL | CANCELLED | paris",       # Null Qty
    "SH-006 | USB-C ADAPTER | 40 | Shipped | NEW YORK",        # Case inconsistency
    "SH-007 | Gaming monitor | 10 | shipped | madrid",
    "SH-008 | 4K Monitor | 15 | n/a | London",                 # Missing Status
]

# Dataset 2: Product Price Catalog (Lookup Table)
product_catalog = {
    "wireless mouse": 25.0,
    "usb-c adapter": 15.0,
    "mechanical keyboard": 80.0,
    "gaming monitor": 300.0,
    "4k monitor": 450.0
}

### YOUR CHALLENGES ###
# Challenge 1
clean_shipment = []
for raw1 in shipment_logs:
    try:
        clean_parts = [p.strip().lower() for p in raw1.split("|")]
        ship_id, product, quantity_str, status, destination = clean_parts
        
        if product == 'n/a':
            product = 'Unknown'
        if status == 'n/a':
            status = 'Unknown'

        try:
            quantity = int(quantity_str)
        except ValueError:
            quantity = 0

        row = {
            'ship_id': ship_id,
            'product': product,
            'quantity': quantity,
            'status': status,
            'destination': destination
        }
        clean_shipment.append(row)
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw1}.")
        continue
"""for item in clean_shipment:
    print(item)"""

# Challenge 2
revenue_report = {}
for row in clean_shipment:
    try:
        destination = row['destination']
        price = product_catalog.get(row['product'], 0)
        total = row['quantity'] * price
        
        revenue_report[destination] = revenue_report.get(destination, 0) + total

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {row}.")
        continue

sorted_final = sorted(revenue_report.items(), key=lambda x: x[1], reverse=True)

for city, money in sorted_final:
    print(f"{city.title()}: ${money}")