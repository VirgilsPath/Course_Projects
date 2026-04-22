from menu import Menu
from franchise import Franchise
from business import Business

master_menu = Menu('El Corazón Master Menu', 800, 2300)

northside_store = Franchise('123 Main St, Chicago', master_menu)
southside_store = Franchise('456 North Ave, Chicago', master_menu)

my_business = Business('El Corazón de la Taco', [northside_store, southside_store])

# 1. Choose an order
order = ["Al Pastor", "Margarita", "Churros"]

# 2. Pick a time (e.g., 10:00 AM - 1000)
test_time = 1000

# 3. Find the store and calculate the bill
store = my_business.find_store("123 Main St, Chicago")
print(f"Testing order at {test_time}...")
print(store.menu.calculate_bills(order, test_time))
