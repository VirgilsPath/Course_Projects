# Functional Transaction Analyzer

A Python-based financial data processor built using **Functional Programming (FP)** principles. This project demonstrates how to handle complex data transformations and calculations without using traditional imperative loops (`for` or `while`), focusing instead on **Recursion** and **Stateless Logic**.

## Project Overview
This project shifts away from standard iterative patterns to master high-level computer science concepts:
1. **Recursive Processing:** Engineered custom recursive algorithms for summation, counting, and list-building to replace traditional looping.
2. **Data Transformation:** Leverages higher-order functions and **Lambda** expressions to extract specific financial subsets.
3. **Stateless Logic:** Every function is "pure," ensuring that the original dataset remains immutable and the program is free of "side effects."
4. **JSON Integration:** Maps persistent external data into a functional pipeline for real-world simulation.

---

## File Structure

- **`transaction_analyzer_maker.py`**
  - A utility script used to generate a mock `transactions.json` dataset containing 50 unique financial entries.
  
- **`analyzer.py`**
  - The core logic engine containing recursive functions and declarative analysis pipelines.

- **`transactions.json`**
  - The financial database containing transaction IDs, categories, and amounts.

---

## Functional Programming Highlights

### **The Power of Recursion**
Instead of using a `for` loop to add up totals, this project uses **Divide-and-Conquer** logic. By utilizing **List Slicing** (`data[1:]`), the functions move through the dataset by calling themselves until they hit a **Base Case**.

### **Immutability & Pure Functions**
In this project, data is treated as read-only. Functions like `get_ids_by_category()` do not modify the original list; instead, they build and return a brand-new list of results. This approach is highly valued in **Distributed Computing** and **Data Engineering** because it prevents bugs caused by shared state.

---

## Skills Mastered
- **Recursive Thinking:** Solving problems by breaking them into smaller, self-referential sub-problems.
- **Higher-Order Functions:** Implementing `filter()` and `map()` to create declarative data pipelines.
- **Immutability:** Managing data flows without modifying global or local variables (No "Side Effects").
- **List Processing:** Utilizing advanced slicing and head/tail recursion patterns to traverse data structures.
