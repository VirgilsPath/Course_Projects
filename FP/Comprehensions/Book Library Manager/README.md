Pythonic Book Library Manager

A data-driven project demonstrating Declarative Programming and List Comprehensions in Python. This project focuses on processing a library dataset through high-performance, one-liner transformations.

Key Features

    Declarative One-Liners: Replaced complex loops with list comprehensions for better readability and performance.

    Data Mapping: Used f-string formatting inside comprehensions to transform dictionary data into human-readable strings.

    Multi-Level Filtering: Combined conditional logic and iteration to extract specific subsets (e.g., specific genres or rating thresholds).

    Set Theory: Implemented set comprehensions to automatically handle duplicate data (e.g., unique author extraction).

Concepts Applied

    List & Set Comprehensions: The standard Pythonic way to handle functional data transformations.

    F-String Interpolation: Dynamic string building within data pipelines.

    JSON Integration: Using external data sources for real-world simulation.

    DRY (Don't Repeat Yourself): Minimizing boilerplate code through efficient syntax.

Project Structure

    book_maker.py: A utility script to generate the books.json dataset.

    book_analyzer.py: The core processing script using one-liner pipelines.

    books.json: A library dataset containing 30 unique book entries.

Example Pipelines

    Genre Filter: [b['title'] for b in data if b['genre'] == 'Fantasy']

    Unique Extraction: {b['author'] for b in data}
    
    Formatted Mapping: [f"{b['title']} by {b['author']}" for b in data if b['genre'] == 'Sci-Fi']