# Personal Finance Manager (CLI)

A command-line Personal Finance Manager built in Python to practice software development fundamentals.

## Features

- Add income transactions
- Add expense transactions
- Choose today's date or enter a custom transaction date
- View all recorded transactions
- Persist transactions using a JSON file
- Automatically creates the transaction database if it doesn't exist
- Handles missing or empty JSON files gracefully

## Technologies Used

- Python 3
- datetime
- json
- pathlib

## Project Structure

```
main.py
transaction_data.json
README.md
```

## Current Workflow

1. Load existing transactions from JSON.
2. Display the main menu.
3. Add Income or Expense.
4. Save transaction immediately.
5. View all stored transactions.
6. Exit application.

## Concepts Practiced

- Functions
- Lists and Dictionaries
- JSON Serialization
- File Handling
- Exception Handling
- Loops
- User Input Validation
- Modular Programming

## Upcoming Improvements

- Refactor duplicated logic
- Better input validation
- Transaction categories
- Monthly summaries
- Income vs Expense reports
- Budget tracking
- CSV export