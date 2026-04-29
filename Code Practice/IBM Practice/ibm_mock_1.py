### IBM-STYLE DATA PLAYGROUND - ROUND 1 ###

# Dataset 1: Messy Cloud Instance Logs
# Format: "Region-InstanceID-Status"
instance_logs = [
    "us-east-101-RUNNING",
    "us-west-202-STOPPED",
    "eu-west-303-running",
    "us-east-404-ERROR",
    "eu-west-505-STOPPED",
    "us-east-606-running"
]

# Dataset 2: Server Usage Data (Nested Dictionary)
# Maps InstanceID to its usage metrics
usage_metrics = {
    "101": {"cpu": 45, "memory": 2048},
    "202": {"cpu": 10, "memory": 512},
    "303": {"cpu": 80, "memory": 4096},
    "404": {"cpu": 0, "memory": 0},
    "505": {"cpu": 5, "memory": 1024},
    "606": {"cpu": 95, "memory": 8192}
}

### YOUR CODE BELOW ###
"""1. Normalization & Count (Word Count Practice):
Create a dictionary called status_counts. Extract the Status from each log in instance_logs.
    Requirement: You must handle the fact that some are lowercase (running) and some are uppercase (RUNNING).
    Goal: {"running": 3, "stopped": 2, "error": 1}.

2. The Substring Join:
Loop through instance_logs. For every instance that is currently running, look up its CPU usage in the usage_metrics dictionary using the InstanceID from the log string.
    Goal: Print Instance [ID] in [Region] is using [CPU]% CPU.

3. Custom Sort:
Create a list of tuples containing (InstanceID, CPU_Usage) for all instances. Sort this list by CPU usage in descending order.

4. Health Check (Logic Practice):
Create a list called high_load_instances containing the IDs of all instances where CPU > 75% or Status is 'ERROR'. """

# Challenge 1
status_counts = {}
for raw1 in instance_logs:
    try:
        region, inst_id, status = raw1.lower().rsplit('-', 2)

        status_counts[status] = status_counts.get(status, 0) + 1

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw1}.")
        continue
print(status_counts)

# Challenge 2
for raw2 in instance_logs:
    try:
        region, inst_id, status = raw2.lower().rsplit('-', 2)
        cpu = usage_metrics[inst_id]['cpu']
        inst_id = int(inst_id)
        if status == "running":
            print(f"Instance {inst_id} in {region} is using {cpu}% cpu.")

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw2}.")
        continue

# Challenge 3
list1 = []
for inst_id, metrics in usage_metrics.items():
    try:
        cpu = metrics['cpu']
        list1.append((inst_id, cpu))
    except (ValueError, KeyError, TypeError):
        print(f"Skipping {inst_id}.")
        continue
list1.sort(key=lambda x: x[1], reverse=True)
print(list1)

# Challenge 4
high_load_instances = []

for raw3 in instance_logs:
    try:
        region, inst_id, status = raw3.lower().rsplit('-', 2)
        cpu = usage_metrics[inst_id]['cpu']
        if cpu > 75 or status == "error":
            high_load_instances.append(inst_id)

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw3}.")
        continue
print(high_load_instances)