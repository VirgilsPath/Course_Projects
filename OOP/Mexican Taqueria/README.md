# El Corazón: Enterprise Restaurant Management

A scalable, multi-file **Object-Oriented Programming (OOP)** project designed to manage a restaurant enterprise. This project focuses on **Object Composition** to link business entities, physical locations, and complex service rules into a unified system.

## Project Overview
This system implements a professional "Tiered Architecture" for business management:
1. **Menu Engineering:** Manages JSON data parsing, price calculations, and time-restricted item availability (Alcohol controls).
2. **Franchise Operations:** Handles physical location data and dynamic "Open/Closed" status checks.
3. **Corporate Management:** A high-level business entity that manages a portfolio of franchises and provides search functionality to locate specific stores.
4. **Data Integration:** Utilizes external JSON files to drive the menu system, allowing for updates without modifying source code.

---

## File Structure

- **`Mexican_Taqueria.py`**
  - The entry point script that initializes the Master Menu and creates the Business portfolio.
  - Simulates a real-world customer order and processes it through the entire hierarchy.
  
- **`menu.py`**
  - The "Engine" of the project.
  - Implements complex billing logic including **Category-Aware Searching** and **Regulatory Time-Gating** (Alcohol service windows).

- **`franchise.py`**
  - Represents the physical store.
  - Acts as the bridge between the Business and the Menu, providing real-time operational status.

- **`business.py`**
  - The "Corporate" layer.
  - Manages a list of `Franchise` objects and implements **Search & Retrieval** algorithms to find stores by address.

- **`menu_data.json`**
  - The external database containing structured categories (Tacos, Alcohol, Dessert) and their respective prices.

---

## OOP Implementation Highlights

### Object Composition
Unlike simple classes, this project uses **Nested Objects**. A `Business` contains a list of `Franchises`, and each `Franchise` contains a `Menu`. This allows a single `Master Menu` change to propagate across the entire enterprise instantly.

### Logical Time-Gating
The system performs a dual-check for every order to ensure business compliance:
```python
# The bill is only calculated if the store is open AND 
# specific items (alcohol) are within their legal service window.
if self.alc_start_time <= current_time <= self.alc_end_time:
    total += self.items["alcohol"][item]
```

---

## Skills Mastered
- **System Architecture:** Designing multi-file projects using **Object Composition** and **Module Imports**.
- **Data Persistence:** Using `json` and `os` modules for fault-tolerant external data handling.
- **Advanced Logic:** Implementing time-based business rules and category-specific search algorithms.
- **Dunder Methods:** Customizing object representation using `__str__` and `__repr__` for clean debugging and reporting.
