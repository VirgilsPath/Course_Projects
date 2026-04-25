# Smart Vending System: State-Pattern Implementation

A high-fidelity simulation of an industrial vending machine. This project utilizes the **State Design Pattern** and **Abstract Base Classes (ABC)** to manage complex logic flows, ensuring the machine behaves differently based on its current operational context (Idle, Transaction, Dispensing, or Maintenance).

## Project Overview
This project moves beyond simple "if/else" logic by implementing a professional **Finite State Machine (FSM)** architecture:

1. **State-Driven Logic:** Behavior is encapsulated in specific state classes. This prevents "illegal" actions, such as entering maintenance mode during a customer transaction.
2. **Intelligent Change-Return:** Implements a **Greedy Algorithm** to dispense the correct physical denominations (Quarters, Dimes, Nickels) based on the machine's real-time `CoinTube` inventory.
3. **Maintenance Interface:** A secured "Back-End" mode that allows for inventory restocking and bank management, demonstrating the separation of User and Administrator interfaces.

---

## File Structure

- **`vending_machine.py`**
  - The core engine containing the `VendingMachine` context and component classes (`Product`, `Slot`, `CoinTube`).
  - Implements the **State Pattern** using classes like `IdleState`, `HasMoneyState`, `DispensingState`, and `MaintenanceState`.
  - Includes a full simulation loop testing transactions, change return, and maintenance refills.

---

## OOP Implementation Highlights

### The State Design Pattern
By delegating tasks to `self.current_state`, the machine avoids "Spaghetti Code." Instead of one giant function with dozens of `if` statements, the logic is cleanly separated into objects that only care about their specific phase of the operation.

### Abstract Base Classes (ABC)
The project uses the `abc` module to define a `VendingState` interface. This ensures that every new state added to the system (like an "Out of Order" state) is forced to handle user inputs (coins, cancellations, selections) consistently.

### Fault-Tolerant Math
The change-making logic handles the common Python floating-point precision issue by using `round(amount, 2)`, ensuring that financial transactions remain accurate down to the cent.

---

## Skills Mastered
- **Design Patterns:** Practical implementation of the **State Pattern** and **FSM**.
- **Abstraction:** Using **Abstract Base Classes** to enforce code structure.
- **Encapsulation:** Managing complex internal hardware components like `CoinTubes` and `Slots`.
- **Greedy Algorithms:** Solving the "Change-Making Problem" by prioritizing the highest denominations first.
