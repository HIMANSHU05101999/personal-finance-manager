def add_transaction(transaction_type: str):
    amount=int(input("Enter amount:"))
    description=input("Enter description:")
    transaction_detail={"type":transaction_type,
                "amount":amount,
                "description":description
                }
    return transaction_detail

def view_transaction():
    return ("You chose View Transactions")

def display_menu():
    print(("\n===== Personal Finance Manager ====="))
    user_choice=int(input("1.Add Income\n2.Add Spends\n3.View Transaction\n4.Exit\nYour Choice: "))
    return user_choice
    

def main():
    
    user_choice=display_menu()

    if user_choice==1:
        income_added=(add_transaction("income"))
        print(income_added)
    elif user_choice==2:
        expense_added=(add_transaction("expense"))
        print(expense_added)
    elif user_choice==3:
        print(view_transaction())
    elif user_choice==4:
        print("Goodbye!")
    else:
        print("Invalid menu option.")

if __name__=="__main__":
    main()