# Virtual Pet: Game Loop & State Management

A classic interactive pet simulation that demonstrates core **Object-Oriented Programming (OOP)** concepts such as **Encapsulation**, **Internal Logic Clamping**, and the implementation of a continuous **Game Loop**.

## Project Overview
This project simulates the lifecycle of a virtual pet, requiring the user to balance three critical internal stats: Hunger, Energy, and Happiness. 
1. **Interactive Loop:** Uses a `while True` loop to process real-time user decisions and advance the game state.
2. **Stat Clamping:** Implements private helper methods to ensure pet attributes stay within a logical range (0-10), preventing data corruption.
3. **Condition-Based Outcomes:** The game dynamically reacts to the pet's state, triggering "Game Over" scenarios if the pet becomes too hungry, sad, or exhausted.

---

## File Structure

- **`virtual_pet.py`**
  - Contains the `Pet` class which encapsulates the pet's attributes and behaviors.
  - Implements the main interactive console interface for player input and status reporting.

---

## Technical Implementations

### **Attribute Clamping (Data Integrity)**
I implemented a private method `_clamp_stats()` using Python’s `min()` and `max()` functions. This ensures that even if a pet "plays" multiple times, their happiness never exceeds 10, and their hunger never drops below 0, maintaining a consistent game balance.

### **Temporal State Decay**
Every action taken by the player triggers a `pass_time()` method. This simulates a "living" entity where time naturally increases hunger and decreases energy/happiness, forcing the player to make strategic choices to keep the pet alive.

### **Robust Input Handling**
The project utilizes `try-except` blocks to handle non-integer user inputs, ensuring the game loop doesn't crash if a user enters an invalid character.

---

## Skills Mastered
- **Class State Management:** Tracking multiple interacting variables within a single object instance.
- **Helper Methods:** Using "private" naming conventions (e.g., `_method_name`) for internal class logic.
- **User Interface Design:** Building a clean, text-based console interface with dynamic status messaging.
- **Game Logic Design:** Implementing win/loss conditions based on attribute thresholds.
