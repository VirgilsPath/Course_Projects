from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Slot:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.max_capacity = 10
    
    def has_item(self):
        return self.quantity > 0

    def add_stock(self, amount):
        if self.quantity + amount > self.max_capacity:
            self.quantity = self.max_capacity
            print(f"Slot full. Stock set to {self.max_capacity}.")
        else:
            self.quantity += amount

class Coin:
    def __init__(self, value):
        self.value = value

class CoinTube:
    def __init__(self, denomination, initial_count):
        self.denomination = denomination
        self.count = initial_count
    
    def add_coin(self):
        self.count += 1
    
    def take_coin(self):
        if self.count > 0:
            self.count -= 1
            return True
        return False # Empty

class VendingState(ABC):
    @abstractmethod
    def insert_coin(self, machine, amount):
        pass

    @abstractmethod
    def select_product(self, machine, slot_index):
        pass

    @abstractmethod
    def cancel(self, machine):
        pass
    
    @abstractmethod
    def enter_maintenance(self, machine, code):
        pass

class VendingMachine:
    def __init__(self, slots):
        self.slots = slots
        self.bank = {
            0.25: CoinTube(0.25, 15),
            0.10: CoinTube(0.10, 15),
            0.05: CoinTube(0.05, 15)
        }

        self.user_balance = 0.0

        self.idle_state = IdleState()
        self.has_money_state = HasMoneyState()
        self.maintenance_state = MaintenanceState()
        self.dispensing_state = DispensingState()

        self.current_state = self.idle_state
    
    def return_change(self, amount_owed):
        denominations = sorted(self.bank.keys(), reverse=True)

        print(f"Dispensing change: ${amount_owed:.2f}")

        for coin_value in denominations:
            tube = self.bank[coin_value]

            while amount_owed >= coin_value and tube.count > 0:
                tube.take_coin()
                amount_owed = round(amount_owed - coin_value, 2)

                print(f"Released: {coin_value}")
        
        if amount_owed > 0:
            print(f"Error: Not enough change in machine! Owed: ${amount_owed}")
        else:
            print("Change return successfull.")

    def set_state(self, state):
        self.current_state = state
    
    def insert_coin(self, amount):
        self.current_state.insert_coin(self, amount)
    
    def select_product(self, index):
        self.current_state.select_product(self, index)

    def cancel_transaction(self):
        self.current_state.cancel(self)

    def enter_maintenance(self, code):
        self.current_state.enter_maintenance(self, code)

class IdleState(VendingState):
    def insert_coin(self, machine, amount):
        machine.user_balance += amount
        machine.set_state(machine.has_money_state)
    
    def select_product(self, machine, slot_index):
        print("Please insert money first.")
    
    def cancel(self, machine):
        print("Nothing to cancel.")

    def enter_maintenance(self, machine, code):
        if code == "1234":
            print("Entering Maintenance Mode...")
            machine.set_state(machine.maintenance_state)
        else:
            print("Invalide Code.")

class HasMoneyState(VendingState):
    def insert_coin(self, machine, amount):
        machine.user_balance += amount
        print(f"Balance updated: ${machine.user_balance:.2f}")
    
    def select_product(self, machine, slot_index):
        # Check if the index is valid
        if 0 <= slot_index < len(machine.slots):
            slot = machine.slots[slot_index]

            # Safely check item and price
            if not slot.has_item():
                print("Sold out!")
            elif machine.user_balance >= slot.product.price:
                machine.set_state(machine.dispensing_state)
                machine.current_state.dispense(machine, slot_index)
            else:
                print("Not enough money.")
        else:
            print("Invalid slot number!")
        
    def cancel(self, machine):
        print(f"Returning ${machine.user_balance:.2f}")
        machine.user_balance = 0.0
        machine.set_state(machine.idle_state)
    
    def enter_maintenance(self, machine, code):
        print("Cannot enter maintenance during a transaction.")

class DispensingState(VendingState):
    def dispense(self, machine, slot_index):
        slot = machine.slots[slot_index]

        # Update Inventory
        slot.quantity -= 1

        # Handle Change
        change_amount = machine.user_balance - slot.product.price
        if change_amount > 0:
            print(f"Dispensing ${change_amount:.2f} in change...")
            machine.return_change(change_amount)
        
        # Success Message
        print(f"Clunk! Your {slot.product.name} has been dispensed.")

        # Clean up
        machine.user_balance = 0.0
        machine.set_state(machine.idle_state)
    
    def insert_coin(self, machine, amount):
        print("Busy dispensing item.")
    
    def select_product(self, machine, slot_index):
        print("Already dispensing.")

    def cancel(self, machine):
        print("Too late to cancel.")

    def enter_maintenance(self, machine, code):
        print("Wait until dispense is finished.")

class MaintenanceState(VendingState):
    def insert_coin(self, machine, amount):
        print("Maintenance mode: Coins rejected.")
    
    def select_product(self, machine, slot_index):
        if 0 <= slot_index < len(machine.slots):
            slot = machine.slots[slot_index]
            slot.add_stock(10) # Top off
            print(f"Refilled {slot.product.name}. Current stock: {slot.quantity}")

            for denom in machine.bank:
                machine.bank[denom].count = 15
            print("All coin tubes refilled to 15 coins.")
        else:
            print("Invalid slot.")
    
    def cancel(self, machine):
        print("Exiting Maintenance Mode.")
        machine.set_state(machine.idle_state)
    
    def enter_maintenance(self, machine, code):
        print("Already in maintenance. Exiting...")
        machine.set_state(machine.idle_state)


# Create items
soda = Product("Soda", 1.25)
chips = Product("Chips", 1.00)

# Load machine
machine_slots = [Slot(soda, 10), Slot(chips, 10)]
vm = VendingMachine(machine_slots)

# Test Scenario
print("Testing Items...")
vm.insert_coin(0.25)
vm.insert_coin(1.00) # Balance is 1.25
vm.select_product(0) # Should dispense Soda

print("")

vm.insert_coin(0.05)
vm.insert_coin(1.00)
vm.select_product(1) # Should dispense Chips

print("")

print("Testing Maintenance...")

print("")

vm.enter_maintenance("1234")
vm.select_product(0) # Refill Soda

print("")

vm.select_product(1) # Refill Chips
vm.current_state.cancel(vm) # Exit