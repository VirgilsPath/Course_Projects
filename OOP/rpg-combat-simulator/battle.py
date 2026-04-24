class Battle:
    def __init__(self, hero, villain):
        self.hero = hero
        self.villain = villain
        self.turn = 1
    
    def start_fight(self):
        while self.hero.health > 0 and self.villain.health > 0:
            print(f"***** Turn {self.turn} *****")
            
            # Health percentage
            hero_hp_perc = (self.hero.health / self.hero._max_health) * 100
            villain_hp_perc = (self.villain.health / self.villain._max_health) * 100

            # Check hero health to use potion or fight
            if hero_hp_perc <= 50 and "Health Potion" in self.hero.inventory:
                self.hero.use_item('Health Potion')
            else:
                if self.hero.stamina < 10:
                    self.hero.rest()
                else:
                    self.hero.attack(self.villain)
            
            # Check villain health
            if self.villain.health == 0:
                print("Villain has been slain!")
                break

            # Check villain health to use potion or fight
            if villain_hp_perc <= 50 and "Health Potion" in self.villain.inventory:
                self.villain.use_item('Health Potion')
            else:
                if self.villain.mana < 15:
                    self.villain.rest()
                else:
                    self.villain.attack(self.hero)

            # Check warrior health
            if self.hero.health == 0:
                print("Hero has been slain. Game Over.")
                break
            
            print(f"Warrior's Health: {self.hero.health}")
            print(f"Villain's Health: {self.villain.health}")

            self.turn += 1

            self.hero._stamina += 5
            self.villain._mana += 5