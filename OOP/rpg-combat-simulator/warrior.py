from character import Character

class Warrior(Character):
    def __init__(self, name, health, stamina):
        super().__init__(name, health)
        self._stamina = stamina
    
    @property
    def stamina(self):
        return self._stamina
    
    def attack(self, target):
        if self._stamina >= 10:
            self._stamina -= 10
            target.take_damage(20)
            print(f"Warrior attacks {target.name} for 20 damage!")
        else:
            print("Not enough stamina!")