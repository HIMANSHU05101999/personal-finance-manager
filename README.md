# Personal Finance Manager

A command-line based Personal Finance Manager built using Python. This project allows users to record income and expenses, view transaction history, and generate financial summaries over different time periods.

## Features

### Transaction Management

* Add Income transactions
* Add Expense transactions
* Store transactions persistently using JSON
* View all saved transactions

### Search & Filter

* Search transactions by date
* Search transactions by transaction type (Income/Expense)

### Financial Summaries

* Overall balance summary
* Summary for a specific date
* Monthly summary
* Custom date range summary

### Input Validation

* Prevents invalid date formats
* Prevents invalid month and year values
* Prevents negative or zero transaction amounts
* Validates custom date ranges

---

## Project Structure

```text
Personal-Finance-Manager/
│
├── main.py
├── transaction_data.json
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python 3
* JSON for data persistence
* Object-Oriented Programming concepts:

  * Classes and Objects
  * Constructors
  * Instance Attributes
  * Methods
  * Encapsulation (initial implementation)
  * Properties (learning phase)

---

## Menu

```text
===== Personal Finance Manager =====

1. Add Transaction
2. View Transaction
3. Balance Summary
4. Search Transaction
5. Exit
```

### Summary Options

```text
1. Overall Summary
2. Summary by Date
3. Summary by Month
4. Custom Range
5. Exit
```

---

## Example Summary Output

```text
Total Income: 32000
Total Expense: 6002
-------------------------
Current Balance: 25998
```

---

## Future Improvements

### Planned Features

* Edit Transactions
* Delete Transactions
* Transaction Categories
* Category-wise Summary
* Sorting Transactions
* CSV Export
* Better OOP Refactoring

### Planned Refactoring

After implementing all planned functionality, the project will be refactored into multiple classes such as:

* `Transaction`
* `TransactionManager`
* `SummaryManager`
* `FileManager`

This will improve maintainability and better demonstrate Object-Oriented Programming principles.

---

## Learning Objectives

This project is being developed alongside the **MOOC.fi Advanced Python Programming** course and serves as a practical implementation of concepts learned during the journey toward becoming a Software Engineer and AI Engineer.

Current concepts applied:

✔ Functions
✔ File Handling
✔ JSON Handling
✔ Classes & Objects
✔ Constructors
✔ Methods
✔ Basic OOP Design
✔ Input Validation
✔ Date Handling with `datetime`

---

## How to Run

```bash
git clone https://github.com/HIMANSHU05101999/personal-finance-manager.git

cd personal-finance-manager

python main.py
```

---

## Author

**Himanshu Kumar Dubey**

This project is part of my Python and Software Engineering learning journey.
