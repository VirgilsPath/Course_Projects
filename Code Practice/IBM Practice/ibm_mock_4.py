### IBM MOCK ASSESSMENT: CLOUD RESOURCE OPTIMIZATION ###

# 1. Cloud Instance Logs (Messy Strings)
# Format: "Timestamp | Instance_ID | Action | Cost"
# Note: Cost can be "null", "pending", or a decimal.
cloud_logs = [
    "2024-05-01 | inst-01 | start | 0.0",
    "2024-05-01 | inst-02 | run | 120.50",
    "2024-05-01 | inst-01 | stop | 45.25",
    "2024-05-02 | inst-03 | run | null",      # Missing Data Trap
    "2024-05-02 | inst-02 | run | 150.00",
    "2024-05-02 | inst-01 | run | pending",   # Bad Data Trap
    "2024-05-03 | inst-04 | run | 300.00",
    "2024-05-03 | inst-02 | stop | 10.00"
]

# 2. Instance Metadata (Dictionary)
# Mapping InstanceID -> Region
instance_metadata = {
    "inst-01": "us-east",
    "inst-02": "us-west",
    "inst-03": "eu-central",
    "inst-04": "us-east"
}

### YOUR TASKS ###

# TASK 1: THE REGIONAL CLEANUP
# Create a dictionary 'region_costs' that sums the total cost per REGION.
# - Requirement: Only include 'run' and 'stop' actions.
# - Requirement: Handle "null" and "pending" costs by treating them as 0.0.
# - Requirement: If an Instance_ID isn't in metadata, skip it.

region_costs = {}
for log in cloud_logs:
    try:
        parts = [p.strip().lower() for p in log.split("|")]
        timestamp, inst_id, action, decimal_str = parts
        region = instance_metadata[inst_id]
        if action != 'start':
            try:
                decimal = float(decimal_str)
            except ValueError:
                decimal = 0.0
            region_costs[region] = region_costs.get(region, 0) + decimal
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {log}.")
        continue
print(region_costs)

# TASK 2: UTILIZATION FREQUENCY
# Create a dictionary 'instance_run_counts' that counts how many times 
# each instance performed a 'run' action.

instance_run_counts = {}
for log in cloud_logs:
    try:
        parts = [p.strip().lower() for p in log.split("|")]
        timestamp, inst_id, action, decimal_str = parts
        if action == 'run':
            try:
                decimal = float(decimal_str)
            except ValueError:
                decimal = 0.0
            instance_run_counts[inst_id] = instance_run_counts.get(inst_id, 0) + 1
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {log}.")
        continue
print(instance_run_counts)

# TASK 3: THE IBM LEADERSHIP REPORT
# Create a list of tuples: (Region, Avg_Cost_Per_Action)
# - Avg_Cost = Total_Regional_Cost / Total_Actions_In_Region
# - Requirement: Sort by Avg_Cost (DESCENDING).
# - TIE-BREAKER: Sort by Region Name (ALPHABETICAL).

region_avg_cost = []
region_per_action = {}
for log in cloud_logs:
    try:
        parts = [p.strip().lower() for p in log.split("|")]
        timestamp, inst_id, action, decimal_str = parts
        region = instance_metadata[inst_id]
        if action != 'start':
            try:
                decimal = float(decimal_str)
            except ValueError:
                decimal = 0.0
            region_per_action[region] = region_per_action.get(region, 0) + 1
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {log}.")
        continue
print(region_per_action)

for region, costs in region_costs.items():
    total_actions = region_per_action[region]
    avg = costs / total_actions
    region_avg_cost.append((region, round(avg, 2)))
sorted_final = sorted(region_avg_cost, key=lambda x: (-x[1], x[0]))
print(sorted_final)

# THE CHALLENGE:
# 1. Update your report to ONLY include data from "2024-05-02" or EARLIER.
# 2. This means the new May 4th log should be ignored.

cloud_logs.append("2024-05-04 | inst-02 | run | 500.00")

may_stats_bf_4 = []
for log in cloud_logs:
    try:
        parts = [p.strip().lower() for p in log.split("|")]
        timestamp, inst_id, action, decimal_str = parts
        year, month, day = [int(t) for t in timestamp.split('-')]
        try:
            decimal = float(decimal_str)
        except ValueError:
            decimal = 0.0
        if day < 4:
            may_stats_bf_4.append(log)
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {log}.")
        continue
print(may_stats_bf_4)