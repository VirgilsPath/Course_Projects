Virtual Pet CLI

A lightweight, Object-Oriented Command Line Interface (CLI) game built in Python. This project demonstrates core OOP principles, state management, and user-input handling.

Features

    Dynamic Stat Tracking: Manage your pet's Hunger, Energy, and Happiness.
    
    OOP Design: Built using a modular Pet class with encapsulated logic.
    
    State Integrity: Implements "clamping" logic to ensure pet stats remain within logical boundaries (0-10).
    
    Game Loop: A persistent interactive loop that simulates the passage of time and aging.


Concepts Demonstrated

    Encapsulation: Keeping pet attributes and behaviors (methods) within a single class.
    
    Helper Methods: Using internal methods (_clamp_stats) to maintain clean, DRY (Don't Repeat Yourself) code.
    
    Conditional Logic: Managing complex game states and "Game Over" conditions based on multiple variables.

How to Run

    Ensure you have Python installed (3.6 or higher).
    
    Clone this repository:
    git clone https://github.com/VirgilsPath/Course_Projects/tree/main/OOP/Virtual%20Pet

    Run the script:
    python3 virtual_pet.py

How to Play

    Feed: Lowers hunger but increases energy.
    
    Play: Increases happiness but costs energy.
    
    Sleep: Fully restores energy.
    
    Watch Out: Every turn, time passes! If hunger hits 10 or happiness hits 0, the game is over.

