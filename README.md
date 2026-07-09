# Personal Finance Manager (Python CLI)

A command-line Personal Finance Manager built with Python to practice software development fundamentals, clean code principles, and file handling before moving to database-backed applications.

## Features

### Transaction Management

* Add new transactions
* Choose transaction type (Income / Expense)
* Enter custom transaction dates or use today's date
* Add transaction descriptions
* Automatically save transactions to a JSON file

### Data Persistence

* Transactions are stored in `transaction_data.json`
* Data persists between program executions
* Automatically creates the database file if it does not exist
* Handles empty or corrupted JSON files gracefully

### View Transactions

* Display all saved transactions
* User-friendly formatted output

### Balance Summary

* Calculate total income
* Calculate total expenses
* Display current balance

### Search Transactions

* Search transactions by date
* Search transactions by transaction type (Income / Expense)

## Technologies Used

* Python 3
* JSON
* pathlib
* datetime

## Project Structure

```text
Personal Finance Manager/
│
├── main.py
├── transaction_data.json
└── README.md
```

## Current Project Status

### Phase 1 ✅

* Project setup
* Add transactions
* JSON data persistence
* View all transactions
* Refactoring of menu and input handling

### Phase 2 (In Progress)

Completed:

* Balance Summary
* Search by Date
* Search by Transaction Type

Upcoming:

* Transaction IDs
* Edit Transaction
* Delete Transaction

### Future Plans

* SQLite database integration
* Monthly reports
* Category-wise summaries
* Budget tracking
* CSV export
* Data visualization
* Unit testing
* Object-Oriented refactoring
* GUI/Web version

## Learning Goals

This project is being developed incrementally to strengthen understanding of:

* Functions
* Modular programming
* File handling
* Exception handling
* JSON data storage
* Data structures
* Code refactoring
* Software design principles
* Version control with Git

## Author

**Himanshu Kumar**

Built as part of my journey toward becoming an AI Engineer while strengthening Python software development fundamentals through real-world projects.
