### IBM MOCK ASSESSMENT - ROUND 3 ###

# Dataset 1: Messy Transaction Logs
# Format: "TransactionType:Amount:Date_Region"
transaction_logs = [
    "Sale:1200.50:2024-05-01_East",
    "Refund:200.00:2024-05-01_West",
    "Sale:invalid:2024-05-02_East",  # Bad data trap!
    "sale:450.75:2024-05-02_East",    # Case sensitivity trap!
    "Refund:150.00:2024-05-03_West",
    "SALE:3000.00:2024-05-03_North",
    "Sale:850.25:2024-05-03_East"
]

# Dataset 2: Region Multipliers
region_multipliers = {
    "East": 1.1,
    "West": 0.9,
    "North": 1.2,
    "South": 1.0
}

### TASK 1: THE NORMALIZED COUNT ###
# Create a dictionary 'type_counts'. 
# Count how many "sale" vs "refund" transactions exist.
# Everything MUST be lowercase so 'SALE' and 'sale' are counted together.

type_counts = {}
for raw1 in transaction_logs:
    try:
        trans_type, amount_str, date_region = raw1.lower().split(':')
        amount = float(amount_str)
        type_counts[trans_type] = type_counts.get(trans_type, 0) + 1
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw1}.")
        continue
print(type_counts)

### TASK 2: THE REVENUE JOIN ###
# Calculate the "Adjusted Revenue" ONLY for "sale" transactions.
# 1. Split the string to get Type, Amount, and the Date_Region chunk.
# 2. Split the Date_Region chunk by "_" to get the Region name.
# 3. Look up the multiplier in 'region_multipliers' based on that region.
# 4. Use try/except to convert the Amount string to a float.
# Calculation: Total = Amount * Multiplier

adjusted_rev = 0
for raw2 in transaction_logs:
    try:
        trans_type, amount_str, date_region = raw2.lower().split(':')
        if trans_type == 'sale':
            amount = float(amount_str)
            region = date_region.split('_')[1].capitalize()
            multiplier = region_multipliers[region]
            total = amount * multiplier
            adjusted_rev += round(total, 2)
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw2}.")
        continue
print(adjusted_rev)

### TASK 3: REGIONAL TOTALS (AGGREGATION) ###
# Create a dictionary 'regional_totals' mapping Region name to its total sale sum.
# Example: {"East": 2500.0, "North": 3600.0}
# Only include "sale" transactions.

regional_totals = {}
for raw3 in transaction_logs:
    try:
        trans_type, amount_str, date_region = raw3.lower().split(':')
        if trans_type == 'sale':
            amount = float(amount_str)
            region = date_region.split('_')[1].capitalize()
            multiplier = region_multipliers[region]
            total = amount * multiplier
            regional_totals[region] = regional_totals.get(region, 0) + round(total, 2)
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw3}.")
        continue
print(regional_totals)

### TASK 4: THE SORTED REPORT ###
# Create a list of tuples: (Region, Total_Sales_Amount).
# Sort the list by the amount in DESCENDING order using a lambda.
# Print the final sorted list.

sorted_report = sorted(regional_totals.items(), key=lambda x: x[1], reverse=True)
print(sorted_report)