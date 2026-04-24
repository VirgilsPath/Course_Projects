# Chicago Crime Data Analysis (From Scratch)

A Python data analysis project focused on simulating and analyzing structured JSON crime data. This project was built without relying on high-level data libraries like Pandas to master the manipulation of native Python dictionaries, lists, and file systems.

## Project Features
- **Synthetic Data Generation:** Generates large, random datasets modeled after real Chicago Open Data formats.
- **Pure Python Algorithms:** Hand-written functions for frequency mapping, filtering, and conditional calculations.
- **Defensive Programming:** Active use of safe file handling and fallback default dictionaries to prevent crashes.

---

## File Structure

- **`bigger_data_maker.py`**
  - Generates the synthetic dataset using the `random` module.
  - Automatically structures the data into a list of dictionaries with parameters like `id`, `crime`, `location`, `district`, and `arrest`.
  - Saves the generated data as `data.json`.
  
- **`read_json_file.py`**
  - The project's core toolbox housing all algorithmic functions used to query the dataset.

- **`tester.py`**
  - The driver script that imports the toolbox, handles data execution, and prints formatted output to the console.

- **`sql_practice.py`**
  - Connects to an in-memory SQLite database.
  - Loads physical JSON data directly into a SQL table.
  - Demonstrates core query writing, including conditional filtering (`WHERE`), counting (`COUNT`), and aggregation sorting (`GROUP BY` / `ORDER BY`).

- **`data.json`**
  - The simulated dataset created by your generator script.

---

## The Custom Python Toolbox (`read_json_file.py`)

Here are the key functions I designed from scratch to process this dataset:

### 1. `load_data()`
Safely opens and loads the local `data.json` file. It utilizes `pathlib` for smart pathing and a `try/except` block to gracefully prevent program crashes if the file is not found.

### 2. `filter_by_condition(dataset, key, value)`
A lightning-fast filter algorithm using a Python list comprehension that returns all rows where a specific key matches a specific value (e.g., finding all crimes in District 3).

### 3. `count_frequencies(dataset, key)`
Builds a frequency tally dictionary. It safely reads row contents using the `.get()` function to ensure the program never crashes if a row is missing data.

### 4. `arrest_rate(dataset, first_key, second_key)`
Calculates the success percentage of arrests within a given slice of data. Includes safety mechanisms to avoid `ZeroDivisionError` and returns a cleanly formatted percentage string.

### 5. `most_frequent_location(dataset, key)` & `most_safe_location(dataset, key)`
These two algorithms track the continuous maximum and minimum occurrences of data keys as they evaluate the dictionary, returning targeted data points.

---

## What I Learned
- Structuring modular, clean, and reusable Python scripts.
- How to efficiently read, write, and safely parse external JSON files.
- The mechanics behind how libraries like Pandas summarize and filter tabular data behind the scenes.
- Mapping counts using dictionaries and tracking dynamic minimum/maximum values.
