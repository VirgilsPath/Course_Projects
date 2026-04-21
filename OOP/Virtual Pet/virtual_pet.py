class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0 # 0 means Full, 10 means Starving
        self.energy = 10
        self.happiness = 10
    
    def feed(self):
        self.hunger -= 3
        self.energy += 1
        self._clamp_stats()
    
    def play(self):
        self.happiness += 2
        self.energy -= 1
        self._clamp_stats()
    
    def sleep(self):
        self.energy += 10
        self._clamp_stats()
    
    def pass_time(self):
        self.hunger += 1 # Hunger going up means hungry
        self.energy -= 1
        self.happiness -= 1
        self._clamp_stats()

        if self.hunger == 10:
            return f"{self.name} is starving."
        elif self.hunger >= 5:
            return f"{self.name} is hungry."
        else:
            return f"{self.name} is okay."
    
    def get_status(self):
        print(f"{self.name}'s Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")

    def _clamp_stats(self):
        self.hunger = max(0, min(10, self.hunger))
        self.energy = max(0, min(10, self.energy))
        self.happiness = max(0, min(10, self.happiness))

# Main Game Loop
my_pet = Pet("Iggy")

while True:
    my_pet.get_status()

    # User input
    print("Please enter a number 1-4")
    try:
        choice = int(input("Do you want to (1) Feed, (2) Play, (3) Sleep, or (4) Exit? "))
    except ValueError:
        print("Please enter the correct numbers.")
        continue

    if choice == 1:
        my_pet.feed()
    elif choice == 2:
        my_pet.play()
    elif choice == 3:
        my_pet.sleep()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    
    status_message = my_pet.pass_time()
    print(status_message)

    if my_pet.energy <= 0 or my_pet.happiness <= 0:
        print(f"Oh no! {my_pet.name} is too exhausted or sad to continue.")
        break

    if my_pet.hunger >= 10:
        print(f"Game Over: {my_pet.name} has run away to find food!")
        break