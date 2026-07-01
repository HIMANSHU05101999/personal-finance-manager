def add_income():
    dictionary={}
    
    transaction_type="Income"
    income=int(input("Enter amount:"))
    description=input("Enter description:")
    #key=["type","amount","description"]
    #value=[transaction_type,income,description]
    #for i in range(len(key)):
    #    dictionary[key[i]]=value[i]
    dictionary={"type":transaction_type,
                "amount":income,
                "description":description
                }
    return dictionary

def add_expense():
    return ("You chose Add Expense")

def view_transaction():
    return ("You chose View Transactions")

def display_menu():
    print(("\n===== Personal Finance Manager ====="))
    user_choice=int(input("1.Add Income\n2.Add Spends\n3.View Transaction\n4.Exit\nYour Choice: "))
    return user_choice
    

def main():
    
    user_choice=display_menu()

    if user_choice==1:
        income_added=(add_income())
        print(income_added)
    elif user_choice==2:
        print(add_expense())
    elif user_choice==3:
        print(view_transaction())
    elif user_choice==4:
        print("Goodbye!")
    else:
        print("Invalid menu option.")

if __name__=="__main__":
    main()