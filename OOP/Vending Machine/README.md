Object-Oriented Vending Machine (Python)

A robust, terminal-based Vending Machine simulation built using the State Design Pattern. This project demonstrates advanced Object-Oriented Programming (OOP) concepts and algorithmic problem-solving.

Key Features

    Dynamic State Management: Uses the State Pattern to handle transitions between Idle, Transaction, Dispensing, and Maintenance modes.

    Greedy Change Algorithm: Implements an optimization algorithm to return the fewest number of coins using available denominations from internal CoinTubes.

    Inventory Control: Manages product Slots with strict capacity limits and real-time stock tracking.

    Admin/Maintenance Mode: Includes a secure access point to refill inventory and restock the machine's change bank.

Technical Concepts Applied

    Encapsulation: Physical components (Coins, Products, Slots) are modeled as individual classes to hide internal logic.

    Inheritance & Abstraction: Utilizes Python's abc module to define a strict interface for all machine states.

    Defensive Programming: Includes validation for invalid slot indices, insufficient funds, and "Sold Out" scenarios.

Class Architecture

    VendingMachine: The "Context" class that coordinates states and holds the bank/inventory.

    VendingState (ABC): The blueprint for all operational modes.
    CoinTube: Manages the physical count of specific coin denominations.

    Slot: Tracks the quantity and max capacity of a specific Product.

How to Run

    Clone the repository:
    git clone https://github.com/VirgilsPath/Course_Projects/tree/main/OOP/Vending%20Machine

    Run the main script:
    python3 vending_machine.py