import json
import os

def get_path():
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, 'menu_data.json')

def load_menu():
    path = get_path()

    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return "File not found."

class Menu:
    def __init__(self, name, start_time, end_time):
        self.name = name
        all_data = load_menu()
        self.items = all_data
        self.start_time = start_time
        self.end_time = end_time
        self.alc_start_time = 1400
        self.alc_end_time = 2200
    
    def calculate_bills(self, purchased_items, current_time):
        if current_time < self.start_time or current_time >= self.end_time:
            return "The restaurant is closed."

        total = 0

        for item in purchased_items:
            if item in self.items.get("alcohol", {}):
                if self.alc_start_time <= current_time <= self.alc_end_time:
                    total += self.items["alcohol"][item]
                else:
                    print(f"Skipping {item}: We can't serve alcohol right now.")
                continue

            found = False
            for category in self.items:
                if category != "alcohol" and item in self.items[category]:
                    total += self.items[category][item]
                    found = True
                    break
            
            if not found:
                print(f"Sorry, we don't have {item} on the menu.")
        
        return (f"${total:.2f}")
    
    def __str__(self):
        return f"The {self.name} menu is available from {self.start_time} to {self.end_time}."
    
    def __repr__(self):
        return self.name