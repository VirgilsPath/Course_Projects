# Financial Data Sanitization Pipeline (ETL)

A robust **Data Cleaning** and **ETL (Extract, Transform, Load)** project designed to handle the "dirty" data typically found in bank exports and corporate spreadsheets. This project demonstrates the ability to sanitize messy strings, handle missing values, and standardize categorical data for downstream analysis.

## Project Overview
This tool automates the transformation of a "chaotic" CSV into a structured, analysis-ready dataset:
1. **Simulation:** A custom generator creates a dataset with intentional errors (missing dates, currency symbols, and inconsistent text casing).
2. **Sanitization Pipeline:** Implements a multi-stage cleaning process to normalize financial amounts and categories.
3. **Data Imputation:** Automatically identifies missing date entries and fills them with logical default values to prevent pipeline failure.
4. **Data Integrity:** Ensures all financial values are converted from strings to high-precision floating-point numbers.

---

## File Structure

- **`dirty_data_maker.py`**
  - The "Chaos Generator." It creates a CSV with 100 records containing missing amounts, symbol-heavy strings (e.g., `"$1,200.50"`), and inconsistent category formatting.
  
- **`finance_cleaner.py`**
  - The core **Sanitization Engine**. It uses custom logic to "wash" the data, stripping unwanted characters and standardizing the schema.
  
- **`dirty_finance_data.csv`**
  - The raw, unformatted input file.

- **`clean_finance_data.csv`**
  - The final, polished output file, ready for SQL querying or Matplotlib visualization.

---

## Data Cleaning Highlights

### Advanced String Sanitization
I developed a "chaining" method to handle currency symbols and thousand-separators simultaneously, ensuring the data is castable to a numeric type:
```python
# Cleans "$1,200.50" -> 1200.5
clean_value = raw_amount.replace("$", "").replace(",", "")
```

### Standardizing Categorical Data
To prevent data fragmentation in SQL (where "FOOD" and "food" are seen as different), the pipeline implements **normalization** logic:
- **`.strip()`**: Removes leading/trailing whitespace.
- **`.lower()`**: Standardizes casing across the entire dataset.

---

## Skills Mastered
- **ETL Workflows:** Managing the flow of data from a raw state to a processed state.
- **Data Imputation:** Handling missing values (**Nulls**) without losing row-level integrity.
- **CSV Module Proficiency:** Mastering `DictReader` and `DictWriter` for structured file manipulation.
- **Fault-Tolerant Logic:** Building functions that handle both clean and dirty inputs without crashing.
