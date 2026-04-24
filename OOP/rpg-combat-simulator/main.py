from warrior import Warrior
from mage import Mage
from battle import Battle

warrior = Warrior('Arthur', 100, 30)
villain = Mage('Dark Wizard', 80, 40)

warrior.add_item('Health Potion')
villain.add_item('Health Potion')

game = Battle(warrior, villain)

game.start_fight()