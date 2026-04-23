from character import Character
from warrior import Warrior
from mage import Mage

# Create Villain
goblin = Character("Goblin", 100)
print(f"A wild {goblin.name} appears with {goblin.health} HP!")

# Creates Heros
warrior = Warrior("Arthur", 100, 15)
wizard = Mage("Gandalf", 80, 20)

# Polymorphism in action. Both use same method name
print("\n***** Battle Starts *****")
warrior.attack(goblin)
wizard.attack(goblin)

# Check the aftermath
print("\n***** Battle Results *****")
print(goblin)
print(f"Arthur's Stamina: {warrior.stamina}")
print(f"Gandalf's Mana: {wizard.mana}")

# Test edge cases (Running out of resources)
print("\n***** Second Attack *****")
warrior.attack(goblin)
wizard.attack(goblin)