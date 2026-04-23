# Sal's Shipping project

while True:
    try:
        weight = float(input("Please enter weight: "))

        if weight <= 0:
            print("Weight cannot be zero or negative. Please try again.")
            continue
        else:
            break

    except ValueError:
        print("Please enter numbers only")

def calculate_ground_shipping(weight):
    if weight <= 2:
        cost = weight * 1.50 + 20.00
    elif weight <= 6:
        cost = weight * 3.00 + 20.00
    elif weight <= 10:
        cost = weight * 4.00 + 20.00
    else:
        cost = weight * 4.75 + 20.00
    return cost

def calculate_premium_ground_shipping(weight):
    # Weight parameter is included for consistency but not used in calculation
    return 125.00

def calculate_drone_shipping(weight):
    if weight <= 2:
        cost = weight * 4.50
    elif weight <= 6:
        cost = weight * 9.00
    elif weight <= 10:
        cost = weight * 12.00
    else:
        cost = weight * 14.25
    return cost

# Calculate costs for all shipping methods
ground_cost = calculate_ground_shipping(weight)
premium_cost = calculate_premium_ground_shipping(weight)
drone_cost = calculate_drone_shipping(weight)

# Print the costs for each
print(f"\nGround Shipping Cost: ${ground_cost:.2f}")
print(f"Premium Ground Shipping Cost: ${premium_cost:.2f}")
print(f"Drone Shipping Cost: ${drone_cost:.2f}")

# Determine the cheapest option and print the result
if ground_cost <= premium_cost and ground_cost <= drone_cost:
    print(f"\nCheapest option: Ground Shipping. Cost: ${ground_cost:.2f}")
elif premium_cost <= ground_cost and premium_cost <= drone_cost:
    print(f"\nCheapest option: Premium Ground Shipping. Cost: ${premium_cost:.2f}")
else:
    print(f"\nCheapest option: Drone Shipping. Cost: ${drone_cost:.2f}")