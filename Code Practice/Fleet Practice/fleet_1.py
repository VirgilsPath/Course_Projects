### ENTRY-LEVEL SCREENING: FLEET MANAGEMENT ###

# 1. Maintenance Logs (Messy Strings)
# Format: "VehicleID | Status | Mileage_since_last_service"
# Note: Mileage might be "n/a" or missing!
logs = [
    "V-101 | Active | 5000",
    "V-102 | Repair | 1200",
    "V-103 | active | 8000",
    "V-104 | Active | n/a",    # Bad data
    "V-105 | retired | 20000", # We should ignore 'retired'
    "V-106 | active | 5000",
    "V-107 | ACTIVE | 1200"
]

# 2. Vehicle Model Map (Dictionary)
# Mapping VehicleID -> Model Name
models = {
    "V-101": "Tesla Model 3",
    "V-102": "Ford F-150",
    "V-103": "Tesla Model 3",
    "V-104": "Chevy Bolt",
    "V-106": "Ford F-150",
    "V-107": "Chevy Bolt"
}

### YOUR TASKS ###

# TASK 1: CLEANING & FILTERING
# Create a dictionary 'model_mileage' that sums the total mileage for 
# each MODEL, but ONLY for vehicles with an 'active' status.
# - Requirement: Handle "n/a" and casing ('Active' vs 'active').
# - Requirement: Use the 'models' dict to group by Model Name, not ID.

model_mileage = {}
for log in logs:
    try:
        parts = [p.strip() for p in log.split("|")]
        vehicle_id, status, mileage_str = parts
        status = status.lower()
        model = models[vehicle_id]
        try:
            mileage = int(mileage_str)
        except ValueError:
            mileage = 0
        if status == 'active':
            model_mileage[model] = model_mileage.get(model, 0) + mileage
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {log}.")
        continue
sorted_model_mileage = dict(sorted(model_mileage.items(), key=lambda x: (-x[1], x[0])))
print(sorted_model_mileage)

# TASK 2: FREQUENCY COUNT
# Create a dictionary 'model_counts' that counts how many ACTIVE 
# vehicles exist for each model.

model_counts = {}
for log in logs:
    try:
        parts = [p.strip() for p in log.split("|")]
        vehicle_id, status, mileage_str = parts
        status = status.lower()
        model = models[vehicle_id]
        if status == 'active':
            model_counts[model] = model_counts.get(model, 0) + 1
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {log}.")
        continue
sorted_model_counts = dict(sorted(model_counts.items(), key=lambda x: (x[0], -x[1])))
print(sorted_model_counts)

# TASK 3: THE MULTI-LEVEL SORT
# Create a list of tuples: (Model_Name, Avg_Mileage)
# - Avg_Mileage = Total_Mileage / Count_of_Vehicles
# - Requirement: Sort the list by Avg_Mileage (DESCENDING).
# - TIE-BREAKER: If mileage is the same, sort by Model Name (ALPHABETICAL).

model_avg_mileage = []

for model, mile in model_mileage.items():
    count = model_counts[model]
    avg = mile / count
    model_avg_mileage.append((model, avg))
sorted_final = sorted(model_avg_mileage, key=lambda x: (-x[1], x[0]))
print(sorted_final)