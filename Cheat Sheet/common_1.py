### 1. CLEAN & SPLIT (The "Multi-Tool") ###
# Handles extra spaces and case sensitivity in one go
"""parts = [p.strip().lower() for p in raw_string.split('|')]"""

### 2. DEFENSIVE MATH (The "Trap Avoider") ###
# Use this when data might be "null", "n/a", or "pending"
"""try:
    value = float(amount_str)
except ValueError:
    value = 0.0"""  # Or skip the row using 'continue'

### 3. LOOKUP & JOIN (The "Bridge") ###
# Safe lookup for IDs or Regions
"""info = mapping_dict.get(key, "Unknown")
if info == "Unknown":
    continue""" # Skip if ID is missing from your metadata

### 4. MULTI-LEVEL SORT (The "Tie-Breaker") ###
# Sort by Number (Desc) then by Name (Asc)
# x[1] is the number, x[0] is the name
"""final_list.sort(key=lambda x: (-x[1], x[0]))"""
