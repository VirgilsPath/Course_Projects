class Character:
    def __init__(self, name, health):
        self.name = name
        self._max_health = health
        self.health = health
        self.inventory = []
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Health must be a number!")
        
        if value < 0:
            self._health = 0
        elif value > self._max_health:
            self._health = self._max_health
        else:
            self._health = value
    
    def take_damage(self, damage_amount):
        self.health -= damage_amount
        return self.health

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up a {item}!")

    def use_item(self, item):
        if item in self.inventory:
            if item == "Health Potion":
                self.health += 20
                self.inventory.remove(item)
                print(f"{self.name} has used a {item} and healed up!")
            else:
                print(f"{item} cannot be used right now.")
        else:
            print("Item not found in inventory!")

    def __repr__(self):
        return f"Character(Name: {self.name}, Health: {self._health})"
    
