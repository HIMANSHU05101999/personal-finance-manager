from datetime import datetime
import json 
from pathlib import Path
def add_transaction(transaction_type: str, date: datetime):
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
    formatted_result=[]
    for transactions in transaction_list:
        date=transactions['date']
        transaction_type=transactions['type']
        amount=transactions['amount']
        description=transactions['description']
        formatted_result.append(
                        f"--------------------------\n"
                        f"Date: {date}\n"
                        f"Transaction Type: {transaction_type}\n"
                        f"Amount: {amount}\n"
                        f"Description: {description}\n"
                        f"--------------------------"
                                )
    return formatted_result

def load_transaction(transaction_file: str):
    try:
        with open(transaction_file) as trans_file:
            database_transaction=json.load(trans_file)
    
    except FileNotFoundError:
            data=[]
            with open(transaction_file,"w") as file:
                json.dump(data, file, indent=4)

    except json.JSONDecodeError:
            return [] 
            
    
def display_menu():
    print(("\n===== Personal Finance Manager ====="))
    user_choice=int(input("1.Add Income\n2.Add Spends\n3.View Transaction\n4.Exit\nYour Choice: "))
    return user_choice
    
def get_transaction_date():
    while True:
        date_choice=int(input("Update Date Press 1 Or Continue with Today's Date Press 2: "))
        if date_choice==1:
            date=input("Enter Date (DD.MM.YYYY): ")
            date=str(datetime.strptime(date,'%d.%m.%Y'))
            return date
        elif date_choice==2:
            return datetime.today().strftime('%d.%m.%Y')
        else:
            print("Invalid Choice Enter Again!!!")

def main():
    transaction_file=Path(__file__).parent/"transaction_data.json"
    transaction_list=load_transaction(transaction_file)
    while True:
        user_choice=display_menu()
        transact_typ=""
        if user_choice==1:
            transact_typ="Income"
        elif user_choice==2:
            transact_typ="Expense"
        elif user_choice==3:
            formatted=view_transaction(transaction_list)
            if formatted!=[]:
                for item in formatted:
                    print(item)
            else:
                print("No Transactions to show.")        
                    
        elif user_choice==4:
            print("Goodbye!!!")
            break
        else:
            print("Invalid menu option.")
        
        if user_choice in(1,2):
            date=get_transaction_date()
            transaction=add_transaction(transact_typ,date)
            save_transaction(transaction,transaction_list,transaction_file)
            
            
                

if __name__=="__main__":
    main()
