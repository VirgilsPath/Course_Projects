from character import Character
from warrior import Warrior

# Created a hero character with taking damage
hero = Character("Arthur", 100)
print(hero)

hero.take_damage(30)
print(hero)

hero.take_damage(150)
print(hero)

# Default character villain to test
villain = Character("Goblin", 50)

# Warrior
warrior_hero = Warrior("Arthur", 100, 15)

print(villain)
print(warrior_hero)

# Warrior attacks villain
warrior_hero.attack(villain)

print(villain)

# Test attack again with less stamina
warrior_hero.attack(villain)
