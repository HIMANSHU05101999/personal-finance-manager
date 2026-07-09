from datetime import datetime
import json 
from pathlib import Path
def add_transaction(transaction_type: str, date: str):
    amount=int(input("Enter amount:"))
    description=input("Enter description:")
    transaction_detail={"date":date,
                "type":transaction_type,
                "amount":amount,
                "description":description
                }
    return transaction_detail

def save_transaction(transaction: dict,transaction_list: list, transaction_file: str):
    transaction_list.append(transaction)
    with open(transaction_file,"w") as trans_file:
        json.dump(transaction_list, trans_file, indent=4)
    

def view_transaction(transaction_list: list):
    if not transaction_list:
        print("No Transactions to Show!")
        return
    for transaction in transaction_list:
            date=transaction['date']
            transaction_type=transaction['type']
            amount=transaction['amount']
            description=transaction['description']
    
            print("--------------------------")
            print(f"Date: {date}")
            print(f"Transaction Type: {transaction_type}")
            print(f"Amount: {amount}")
            print(f"Description: {description}")
            print(f"--------------------------")
    
    

def load_transaction(transaction_file: str):
    try:
        with open(transaction_file) as trans_file:
            database_transaction=json.load(trans_file)
            return database_transaction
        
    except FileNotFoundError:
            data=[]
            with open(transaction_file,"w") as file:
                json.dump(data, file, indent=4)
                return data
    except json.JSONDecodeError:
            return [] 
    
def display_menu():
    print(("\n===== Personal Finance Manager ====="))
    user_choice=int(input("1.Add Transaction\n2.View Transaction\n3.Balance Summary\n4.Search Teansaction\n5.Exit\nYour Choice: "))
    return user_choice
    
def get_transaction_date():
    while True:
        date_choice=int(input("Press 1: Update Date\nPress 2: Continue with Today's Date\n Choose: "))
        if date_choice==1:
            date=input("Enter Date (DD.MM.YYYY): ")
            date=datetime.strptime(date,'%d.%m.%Y')
            return date.strftime("%d.%m.%Y")
        elif date_choice==2:
            return datetime.today().strftime('%d.%m.%Y')
        else:
            print("Invalid Choice Enter Again!!!")

def get_transaction_type():
    while True:
        trans_type=int(input("Press 1: Income\nPress 2: Expense\n Choose:"))
        if trans_type==1:
            transact_typ="Income"
            break
        elif trans_type==2:
            transact_typ="Expense"
            break
        else:
            print("Invalid Entry")
    return transact_typ

def balance_summary(transaction_list: list):
    income=0
    expense=0
    if not transaction_list:
        print("No Transaction Available")
        return
    for transaction in transaction_list:
        if transaction['type']=="Income":
            income += transaction['amount']
        elif transaction["type"] == "Expense":
            expense += transaction['amount']

    print(f"Total Income:",income)
    print(f"Total Expense:",expense)
    print("-"*25)
    print("Current Balance:",income-expense)
        
def filter_transaction(transaction_list: list):
    while True:
        filter_choice=int(input("Press 1. Date\nPress 2. Type\nPress 3. Back\n Choice:"))
        if filter_choice==1:
            try:
                date=input("Enter Date\n(DD.MM.YYYY:)")
                filter_date=datetime.strptime(date,'%d.%m.%Y')
                filter_by_date(transaction_list,filter_date)
            except ValueError:
                print("Invalid Date Format")       

        elif filter_choice==2:
            pass
        elif filter_choice==3:
            print("Returning...")
            return
        else:
            print("Invalid Entry")
        

def filter_by_date(transaction_list: list, date: datetime):
    view_list=[]
    #filter_date=datetime.strptime(date,'%d.%m.%Y')
    for transaction in transaction_list:
        if datetime.strptime(transaction['date'],'%d.%m.%Y')==date:
            view_list.append(transaction)
    
    if not view_list:
        print("No Transaction Available")
    else:
        view_transaction(view_list)


def main():
    transaction_file=Path(__file__).parent/"transaction_data.json"
    transaction_list=load_transaction(transaction_file)
    while True:
        user_choice=display_menu()
        #user_choice=4
        if user_choice==1:
            transact_type=get_transaction_type()
            date=get_transaction_date()
            transaction=add_transaction(transact_type,date)
            save_transaction(transaction,transaction_list,transaction_file)

        elif user_choice==2:
            view_transaction(transaction_list)      
        elif user_choice==3:
            balance_summary(transaction_list)          
        elif user_choice==4:
            filter_transaction(transaction_list)
        elif user_choice==5:
            print("Goodbye!!!")
            break
        else:
            print("Invalid menu option.")
    

if __name__=="__main__":
    main()
