from character import Character

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self._mana = mana

    @property
    def mana(self):
        return self._mana

    def attack(self, target):
        if self._mana >= 15:
            self._mana -= 15
            target.take_damage(30)
            print(f"Mage attacks {target.name} for 30 damage!")
        else:
            print("Not enough mana!")