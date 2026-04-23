from character import Character
from warrior import Warrior
from mage import Mage

warrior = Warrior('Arthur', 100, 30)
villain = Mage('Dark Wizard', 80, 40)

turn = 1

while warrior.health > 0 and villain.health > 0:
    print(f"***** Turn {turn} *****")
    
    # Call warrior attack
    warrior.attack(villain)

    # Check villain health
    if villain.health == 0:
        print("Villain has been slain!")
        break
    
    # Call villain attack
    villain.attack(warrior)

    # Check warrior health
    if warrior.health == 0:
        print("Hero has been slain. Game Over.")
        break
    
    print(f"Warrior's Health: {warrior.health}")
    print(f"Villain's Health: {villain.health}")

    turn += 1

    warrior._stamina += 5
    villain._mana += 5