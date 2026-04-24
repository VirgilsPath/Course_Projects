from character import Character

class Warrior(Character):
    def __init__(self, name, health, stamina):
        super().__init__(name, health)
        self.stamina = stamina
    
    @property
    def stamina(self):
        return self._stamina
    
    @stamina.setter
    def stamina(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Stamina must be a number!")
        
        if value < 0:
            self._stamina = 0
        else:
            self._stamina = value

    def attack(self, target):
        if self._stamina >= 10:
            self._stamina -= 10
            target.take_damage(25)
            print(f"Warrior attacks {target.name} for 25 damage!")
        else:
            print("Not enough stamina!")
    
    def use_item(self, item):
        if item in self.inventory:
            if item == "Stamina Potion":
                self._stamina += 15
                self.inventory.remove(item)
                print(f"{self.name} has used a {item} and gained stamina!")
            else:
                super().use_item(item)
        else:
            print("Item not found in inventory!")
    
    def rest(self):
        self._stamina += 25
        print(f"{self.name} takes a turn to rest and catch his breath!")