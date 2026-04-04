class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __str__(self):
    return (f"{self.name} menu available from {self.start_time} to {self.end_time}.")

  def __repr__(self):
    return self.name

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return (f"${total:.2f}")

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def __str__(self):
    return (f"Address: {self.address}")

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu)
    return available

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __str__(self):
    return (f"Name: {self.name} | Franchises: {self.franchises}")

brunch_menu = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
  }

early_bird_menu = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
  }

dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
  }

kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
  }

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
  }


brunch = Menu('brunch', brunch_menu, 1100, 1600)
early_bird = Menu('early_bird', early_bird_menu, 1500, 1800)
dinner = Menu('dinner', dinner_menu, 1700, 2300)
kids = Menu('kids', kids_menu, 1100, 2100)
arepas = Menu('arepas', arepas_menu, 1000, 2000)

print(brunch)
print(early_bird)
print(dinner)
print(kids)
print(arepas)

# orders
brunch_order = ['pancakes', 'home fries', 'coffee']
print(brunch.calculate_bill(brunch_order))

early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird.calculate_bill(early_bird_order))

arepas_order = ['guayanes arepa', 'jamon arepa']
print(arepas.calculate_bill(arepas_order))

# Franchise exercise
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)
arepas_place = Franchise('189 Fitzgerald', [arepas])

print(flagship_store)
print(new_installment)
print(arepas_place)

print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))
print(arepas_place.available_menus(1200))

# Business exercise
franchises = [flagship_store, new_installment]

basta_fazoolin = Business("Basta Fazoolin' with my heart", franchises)
arepas_business = Business("Take a' Arepa", [arepas_place])

print(basta_fazoolin)
print(arepas_business)