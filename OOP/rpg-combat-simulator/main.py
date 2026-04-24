from character import Character
from warrior import Warrior
from mage import Mage

warrior = Warrior('Arthur', 100, 30)
villain = Mage('Dark Wizard', 80, 40)

warrior.add_item('Health Potion')
villain.add_item('Health Potion')

turn = 1

while warrior.health > 0 and villain.health > 0:
    print(f"***** Turn {turn} *****")
    
    # Health percentage
    warrior_hp_perc = (warrior.health / warrior._max_health) * 100
    villain_hp_perc = (villain.health / villain._max_health) * 100

    # Check health to use potion or fight
    if warrior_hp_perc <= 50 and "Health Potion" in warrior.inventory:
        warrior.use_item('Health Potion')
    else:
        warrior.attack(villain)
    
    if villain_hp_perc <= 50 and "Health Potion" in villain.inventory:
        villain.use_item('Health Potion')
    else:
        villain.attack(warrior)

    # Check villain health
    if villain.health == 0:
        print("Villain has been slain!")
        break

    # Check warrior health
    if warrior.health == 0:
        print("Hero has been slain. Game Over.")
        break
    
    print(f"Warrior's Health: {warrior.health}")
    print(f"Villain's Health: {villain.health}")

    turn += 1

    warrior._stamina += 5
    villain._mana += 5