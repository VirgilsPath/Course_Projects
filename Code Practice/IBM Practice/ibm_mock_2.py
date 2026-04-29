### MOCK TEST DATA  - ROUND 2 ###

# Drone Fleet Status (Messy Strings)
# Format: "ModelName_DroneID_STATUS"
drones = [
    "SkyHawk_D10_Active",
    "SeaGull_D22_Maintenance",
    "SkyHawk_D35_active",
    "Bolt_D40_ACTIVE",
    "SeaGull_D50_Maintenance",
    "Bolt_D62_active"
]

# Battery Levels
# Maps DroneID (String) to Battery Percentage
battery_levels = {
    "D10": 85,
    "D22": 10,
    "D35": 92,
    "D40": 45,
    "D50": 5,
    "D62": 78
}

### YOUR TASKS ###

# 1. Count how many drones are "active" vs "maintenance" (ignore case).
# 2. Create a list of tuples for ONLY ACTIVE drones: (DroneID, Battery_Level).
# 3. Sort that list by Battery Level in DESCENDING order (highest battery first).
# 4. Print the final sorted list.

# Challenge 1
drone_status = {}
for raw1 in drones:
    try:
        model_name, drone_id, status = raw1.lower().split('_')
        drone_status[status] = drone_status.get(status, 0) + 1

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw1}.")
        continue
print(drone_status)

# Challenge 2
list1 = []
for raw2 in drones:
    try:
        model_name, drone_id, status = raw2.split('_')
        status = status.lower()
        batt_perc = battery_levels[drone_id]
        if status == "active":
            list1.append((drone_id, batt_perc))

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw2}.")
        continue
print(list1)

# Challenge 3
list1.sort(key=lambda x: x[1], reverse=True)

# Challenge 4
print(list1)