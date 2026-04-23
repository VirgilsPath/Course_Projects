class Character:
    def __init__(self, name, health):
        self.name = name
        self._health = health
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value
    
    def take_damage(self, damage_amount):
        self.health -= damage_amount
        return self.health

    def __repr__(self):
        return f"Character(Name: {self.name}, Health: {self._health})"
    
