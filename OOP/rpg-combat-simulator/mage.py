from character import Character

class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Mana must be a number!")
        
        if value < 0:
            self._mana = 0
        else:
            self._mana = value

    def attack(self, target):
        if self._mana >= 15:
            self._mana -= 15
            target.take_damage(30)
            print(f"Mage attacks {target.name} for 30 damage!")
        else:
            print("Not enough mana!")
    
    def use_item(self, item):
        if item in self.inventory:
            if item == "Mana Potion":
                self._mana += 15
                self.inventory.remove(item)
                print(f"{self.name} has used a {item} and gained mana!")
            else:
                super().use_item(item)
        else:
            print("Item not found in inventory!")
    
    def rest(self):
        self._mana += 25
        print(f"{self.name} channels energy to restore his mana!")