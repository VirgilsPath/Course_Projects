### DATA STRUCTURES CHALLENGE ###

# 1. Raw Logs (List of Strings)
# Format: "Timestamp | User_ID | Action | Credits_Used"
user_logs = [
    "2024-05-01 | user_01 | login | 0",
    "2024-05-01 | user_02 | upload | 15",
    "2024-05-01 | user_01 | download | 5",
    "2024-05-02 | user_03 | login | 0",
    "2024-05-02 | user_02 | download | 5",
    "2024-05-02 | user_01 | upload | 15",
    "2024-05-03 | user_04 | login | 0",
    "2024-05-03 | user_02 | upload | 15"
]

# 2. Banned Users (Set)
# We need to filter these out!
banned_ids = {"user_04", "user_09"}

# 3. User Names (Dictionary)
# Mapping ID to Real Name
user_profiles = {
    "user_01": "Alice",
    "user_02": "Bob",
    "user_03": "Charlie"
}

### YOUR CODE BELOW ###
"""Task 1
The Set Filter (Uniqueness):
Create a Set called active_users that contains the IDs of everyone who performed an action in the logs.

    Requirement: Do NOT include users in the banned_ids set.
    Goal: Prove you can deduplicate data using a set."""

active_users = set()
for raw_str in user_logs:
    try:
        parts = [p.strip() for p in raw_str.split('|')]
        timestamp, user_id, action, credits_used_str = parts
        if user_id not in banned_ids:
            active_users.add(user_id)

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw_str}.")
        continue

print(active_users)

"""Task 2
The Aggregator (Dictionary Mapping):
Create a Dictionary called user_credits that sums up the total credits used by each user.

    Requirement: Skip any user that isn't in your user_profiles dictionary (use .get() or if in).
    Goal: Prove you can sum values based on a key."""

user_credits = {}
for raw_str in user_logs:
    try:
        parts = [p.strip() for p in raw_str.split('|')]
        timestamp, user_id, action, credits_used_str = parts
        credits_used = int(credits_used_str)
        name = user_profiles.get(user_id)
        if name:
            user_credits[user_id] = user_credits.get(user_id, 0) + credits_used

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {raw_str}.")
        continue
print(user_credits)

"""Task 3
The List Join (Reporting):
Create a List of Tuples formatted as (Real_Name, Total_Credits).

    Goal: Use your user_credits and user_profiles to "join" the data."""

reporting_list = []
for user_id, total in user_credits.items():
    try:
        real_name = user_profiles[user_id]
        reporting_list.append((real_name, total))

    except (ValueError, KeyError, TypeError):
        print(f"Skipping {user_id}.")
        continue
print(reporting_list)

"""Task 4
The Final Sort:
Sort that list of tuples by Total_Credits in descending order.

    Goal: Practice your lambda sort."""

sorted_final = sorted(reporting_list, key=lambda x: x[1], reverse=True)
print(sorted_final)