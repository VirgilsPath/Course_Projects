# Corporate Expense Tracker & Risk Analyzer

A relational data analysis project that simulates a corporate accounting environment. This project focuses on linking disparate datasets (Departments & Expenses) to identify financial overspending using SQL and Python visualization.

## Project Overview
This tool performs a "Full-Stack" data lifecycle:
1. **Simulation:** Generates 200+ synthetic transactions and department budgets.
2. **Relational Engineering:** Designs a two-table SQLite schema (Foreign Key relationship).
3. **Complex Querying:** Utilizes SQL Joins, Aggregations (SUM), and `HAVING` clauses.
4. **Visualization:** Generates an automated Risk Report chart using `Matplotlib`.

---

## File Structure

- **`finance_data_maker.py`**
  - Generates `departments.json` and `expenses.json`.
  - Implements `datetime` logic for a year-to-date transaction history.
  
- **`finance_analysis.py`**
  - The core engine that builds the in-memory SQL database.
  - Links the "Fact Table" (Expenses) to the "Lookup Table" (Departments).
  
- **`deficit_chart.png`**
  - The visual output showing departments that have exceeded their budget by more than $40,000.

---

## Data Analysis Highlights

### Relational Joins
Unlike basic analysis, this project uses a `JOIN` on `dept_id` to translate raw ID numbers into human-readable department names (e.g., changing "ID 2" to "Engineering").

### The "Executive Summary" Query
I developed a complex SQL query to calculate the real-time "Remaining Balance" for each department:
```sql
SELECT 
    dept_name, 
    SUM(amount), 
    budget, 
    (budget - SUM(amount)) AS Remaining
FROM expenses
JOIN departments ON expenses.dept_id = departments.dept_id
GROUP BY dept_name
HAVING Remaining < -40000;
```

---

## Skills Mastered
- **Relational Databases:** Designing schemas for multiple connected tables.
- **Advanced SQL:** Using `GROUP BY`, `ORDER BY`, and `HAVING` for financial reporting.
- **Data Visualization:** Mapping SQL result tuples into `Matplotlib` bar charts.
- **Defensive Coding:** Using `ROUND()` and `Aliasing` for clean, professional reports.
