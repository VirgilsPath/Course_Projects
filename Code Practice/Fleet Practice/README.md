# Logistics & Operations Analytics

This suite of assessments focuses on the movement of physical goods and assets, requiring precise math and chronological data filtering.

## Project Components
1.  **Fleet Management**: Calculating average mileage per vehicle model while ignoring "retired" or "maintenance" statuses.
2.  **Supply Chain Optimization**: Analyzing shipment logs for "shipped" vs "pending" items to calculate regional delivery speeds.
3.  **Warehouse Inventory**: Frequency counts and revenue lookups for SKU-based stock logs.

## Key Logic Patterns
*   **Multi-Level Sorting**: Implementing `key=lambda x: (-x[1], x[0])` to rank performance while keeping names alphabetical.
*   **Date Normalization**: Filtering logs chronologically (e.g., "only data before May 2nd") using string-based timestamp comparisons.
*   **Nested Aggregation**: Managing two dictionaries simultaneously (e.g., `total_miles` and `vehicle_count`) to derive derived metrics like Averages.
