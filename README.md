# Personal Finance Manager (CLI)

A command-line based Personal Finance Manager built using Python. The project helps users record and manage their personal income and expenses, view summaries, search transactions, and maintain persistent financial records using JSON storage.

---

## Features

### Transaction Management

* Add Income and Expense transactions
* Automatic Transaction ID generation
* Delete transactions using Transaction ID
* Persistent storage using JSON files

### Transaction Information

Each transaction stores:

* Transaction ID
* Date
* Transaction Type (Income/Expense)
* Amount
* Description

---

## Summary Features

### Overall Summary

Displays:

* Total Income
* Total Expense
* Current Balance

### Summary by Date

View financial summary for a specific date.

### Summary by Month

View financial summary for a specific month and year.

### Custom Date Range Summary

Generate summaries between two custom dates.

---

## Search Features

Search transactions by:

* Date
* Transaction Type

---

## Validation Implemented

### Amount Validation

* Amount must be greater than 0.
* Invalid numeric input is handled.

### Date Validation

* Supports `DD.MM.YYYY` format.
* Invalid dates and date ranges are handled.

### Month and Year Validation

* Month restricted between `1-12`.
* Year validation added.

### Transaction Deletion Validation

* Invalid IDs handled.
* User confirmation before deletion.
* Graceful handling when transaction does not exist.

### Backward Compatibility

Older transaction records without Transaction IDs are still supported.

---

## Concepts Practiced

This project is being developed alongside the **MOOC.fi Advanced Python** course and currently implements concepts such as:

* Classes and Objects
* Constructors (`__init__`)
* Encapsulation
* Private Attributes
* Instance Methods
* `__str__` Method
* JSON File Handling
* Exception Handling (`try-except`)
* Functions and Modular Programming
* Lists and Dictionaries
* Date Handling using `datetime`
* Persistence using JSON files
* Enumerate
* Type Hints

---

## Project Structure

```text
personal-finance-manager/
│
├── main.py
├── transaction_data.json
├── README.md
└── .gitignore
```

---

## Sample Transaction Record

```json
{
    "id": 5,
    "date": "19.07.2026",
    "type": "Expense",
    "amount": 500,
    "description": "Books"
}
```

---

## Current Menu

```text
===== Personal Finance Manager =====

1. Add Transaction
2. View Transaction
3. Balance Summary
4. Search Transaction
5. Delete Transaction
6. Exit
```

---

## Future Improvements

Planned features:

* Edit Transaction
* Category System (Food, Bills, Salary, Shopping, etc.)
* Export transactions to CSV
* Budget Tracking
* Monthly Reports
* Statistics and Analytics
* Transaction Sorting
* Recurring Transactions
* Full Object-Oriented Refactoring
* SQLite Database Integration
* GUI Version (Tkinter/Web App)

---

## Learning Goal

This project is primarily being developed as a learning project to strengthen understanding of:

* Python Programming
* Object-Oriented Programming
* Data Persistence
* Software Design
* Building Real-World CLI Applications

---

## Author

**Himanshu Kumar Dubey**

BCA Graduate | MCA Student
Aspiring Software Engineer / AI Engineer
