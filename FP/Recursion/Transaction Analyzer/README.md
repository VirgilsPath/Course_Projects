Functional Transaction Analyzer

A Python-based financial data processor built using Functional Programming (FP) principles. This project demonstrates how to handle data transformations and calculations without using traditional imperative loops (for or while), focusing instead on recursion and pure functions.

Key Features

    Recursive Processing: Implemented custom recursive algorithms for summation, counting, and list-building.

    Data Transformation: Uses higher-order functions (filter, lambda) to extract specific data subsets.

    JSON Integration: Handles persistent data storage by reading from and writing to JSON files.

    Stateless Logic: Every function is "pure," meaning it returns a new value rather than modifying the existing state or global variables.

Concepts Applied

    Immutability: Treating data as read-only to prevent bugs caused by "side effects."

    Recursion: Using base cases and recursive steps to solve problems through divide-and-conquer.

    Higher-Order Functions: Leveraging built-in Python tools like filter() to create declarative pipelines.

    List Slicing: Using data[1:] to manage data flow through the recursive stack.

Project Structure

    transaction_analyzer_maker.py: A utility script to generate the initial transactions.json dataset.

    analyzer.py: The core logic file containing the recursive functions and analysis pipelines.

    transactions.json: The mock financial dataset containing 50 unique transactions.

Example Functions

    recursive_sum(): Calculates total balance.
    
    sum_by_category(): Demonstrates conditional branching within recursion.

    get_ids_by_category(): A recursive "map + filter" implementation that builds a new list of IDs.