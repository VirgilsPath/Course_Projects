## RPG Combat Simulator

A terminal-based RPG combat engine built in Python to practice advanced Object-Oriented Programming (OOP) concepts. This project demonstrates how distinct character classes can interact, manage their own protected states, and execute dynamic combat behaviors.

## Key Features

*   **Encapsulation:** Used Python `@property` decorators and "protected" variables (e.g., `_health`) to prevent direct, illegal modifications to character data.
*   **Inheritance:** Leveraged a master `Character` base class to pass down core properties to specialized `Warrior` and `Mage` subclasses without duplicating code.
*   **Polymorphism:** Engineered a unified `attack()` method across different subclasses. The system automatically executes distinct, class-specific attack logic without hardcoding specific checks.
*   **Interactive State Management:** Attack behaviors realistically consume class-specific resources (stamina or mana) and modify the health state of targeted opponent objects.
*   **Interactive Turn-Based Loop:** Integrated a fully automated battle sequence in main.py that simulates dynamic combat rounds, tracks a "turn" counter, and manages automated resource regeneration.
*   **Automated Decision-Making (AI):** Programmed a basic behavioral tree in the combat loop that forces characters to evaluate their health percentage and intelligently choose between self-preservation (healing) and attacking.
*   **Object-Oriented Inventory Grid:** Engineered an inventory array in the master class that allows independent tracking and consumption of strings as active game items.

## Project Structure

*   `character.py` - The base blueprint handling health rules and name definitions.
*   `warrior.py` - The stamina-based physical attacker subclass.
*   `mage.py` - The mana-based magical attacker subclass.
*   `main.py` - The game engine execution file that simulates the actual combat interactions.

## How to Run

1. Clone this repository or download the files.
2. Open your terminal in the project folder.
3. Run the following command:
   ```bash
   python3 main.py
   ```
