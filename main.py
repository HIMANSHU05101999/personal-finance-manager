from datetime import datetime
import json 
from pathlib import Path

#Refactored the program in class and implemented class transaction as per last concepts I learned.
class Transaction():
    def __init__(self, date: str, trans_type: str, amount: int, description: str, transaction_id: int):
        self.__id=transaction_id
        self.__date=date
        self.__trans_type=trans_type
        self.__amount=amount
        self.__description=description

    def to_dict(self):
        return{ "id":self.__id,
                "date":self.__date,
                "type":self.__trans_type,
                "amount":self.__amount,
                "description":self.__description
                }

    def __str__(self):
        return (f"--------------------------\nID: {self.__id}\nDate: {self.__date}\nTransaction Type: {self.__trans_type}\nAmount: {self.__amount}\nDescription: {self.__description}\n--------------------------")



def add_transaction(transaction_type: str, date: str, transaction_id: int):
    
    while True:
        try:
            amount=int(input("Enter amount:"))
            if amount<=0:
                print("Amount should be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid Amount")

    description=input("Enter description:")
    #transaction_detail={"date":date,
    #            "type":transaction_type,
    #            "amount":amount,
    #            "description":description
    #            }
    # Refactoring in Class Phase 1
    transaction_detail=Transaction(date,transaction_type,amount,description,transaction_id) # Object of Transaction
    return transaction_detail # Return Object of class transacation

def save_transaction(transaction: dict,transaction_list: list, transaction_file: str):
    transaction_list.append(transaction)
    with open(transaction_file,"w") as trans_file:
        json.dump(transaction_list, trans_file, indent=4)
    
def view_transaction(transaction_list: list):
    if not transaction_list:
        print("No Transactions to Show!")
        return
    
    for transaction in transaction_list:
            if "id" in transaction:
                id=transaction['id']
                date=transaction['date']
                transaction_type=transaction['type']
                amount=transaction['amount']
                description=transaction['description']
    
                print("--------------------------")
                print(f"ID: {id}")
                print(f"Date: {date}")
                print(f"Transaction Type: {transaction_type}")
                print(f"Amount: {amount}")
                print(f"Description: {description}")
                print(f"--------------------------")
            else:
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
    user_choice=int(input("1.Add Transaction\n2.View Transaction\n3.Balance Summary\n4.Search Transaction\n5.Delete Transaction\n6.Exit\n Your Choice: "))
    return user_choice
    
def get_transaction_date():
    while True:
        date_choice=int(input("Press 1: Continue with Today's Date\nPress 2: Update Date\n Choose: "))
        if date_choice==2:
            date=input("Enter Date (DD.MM.YYYY): ")
            date=datetime.strptime(date,'%d.%m.%Y')
            return date.strftime("%d.%m.%Y")
        elif date_choice==1:
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

def summary_menu(transaction_list: list):
    while True:
        summary_choice=int(input("1.Overall Summary\n2.Summary by Date\n3.Summary by Month\n4.Custom Range\n5.Exit\n Choice: "))
        if summary_choice==1:
            return balance_summary(transaction_list)
        elif summary_choice==2:
            while True:
                try:
                    date=input("Enter Date\n(DD.MM.YYYY:)")
                    filter_date=datetime.strptime(date,'%d.%m.%Y')
                    filtered_list=filter_by_date(transaction_list,filter_date)
                    balance_summary(filtered_list)
                    return
                except ValueError:
                    print("Invalid Date Format")     
        elif summary_choice==3:
                try:
                    mon=int(input("Enter Month(1-12)\n"))
                    if mon<1 or mon>12:
                        raise ValueError ("Invalid Month")
                    yr=int(input("Enter Year(YYYY)\n"))
                    if yr < 1000 or yr > 9999:
                        raise ValueError ("Invalid Year")
                    filtered_list= monthly_summary(transaction_list,mon,yr)
                    balance_summary(filtered_list)
                    return
                except ValueError:
                    print("Invalid Month or Year")
        elif summary_choice==4:
            while True:
                try:
                    s_date=input("Enter Start Date\n(DD.MM.YYYY:)")
                    start_date=datetime.strptime(s_date,'%d.%m.%Y')
                    e_date=input("Enter End Date\n(DD.MM.YYYY:)")
                    end_date=datetime.strptime(e_date,'%d.%m.%Y')
                    if start_date>end_date:
                        raise ValueError
                    filtered_list=custom_range_summary(transaction_list,start_date,end_date)
                    balance_summary(filtered_list)
                    return
                except ValueError:
                    print("Invalid Date Format or Date Range")
        elif summary_choice==5:
            print("Returning...")
            break
        else:
            print("Invalid Choice")  

def custom_range_summary(transaction_list: list, sdate: datetime, edate: datetime):
    view_list=[]
    for transaction in transaction_list:
        if sdate<=datetime.strptime(transaction['date'],'%d.%m.%Y')<=edate:
            view_list.append(transaction)
    return view_list

def monthly_summary(transaction_list: list, mon: int, yr: int):
    view_list=[]
    for transaction in transaction_list:
        if datetime.strptime(transaction['date'],'%d.%m.%Y').month==mon and datetime.strptime(transaction['date'],'%d.%m.%Y').year==yr:
            view_list.append(transaction)
    return view_list
                    
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
                filtered_list=filter_by_date(transaction_list,filter_date)
                if filtered_list:
                    view_transaction(filtered_list)
                else:
                    print("No Transaction")
            except ValueError:
                print("Invalid Date Format")       

        elif filter_choice==2:
            transaction_type=get_transaction_type()
            filter_by_type(transaction_list,transaction_type)
        elif filter_choice==3:
            print("Returning...")
            return
        else:
            print("Invalid Entry")
          
def filter_by_type(transaction_list: list, transaction_type: str):
    view_list=[]
    for transaction in transaction_list:
        if transaction['type']==transaction_type:
            view_list.append(transaction)
    
    if not view_list:
        print("No Transaction Available")
    else:
        view_transaction(view_list)

def filter_by_date(transaction_list: list, date: datetime):
    view_list=[]
    for transaction in transaction_list:
        if datetime.strptime(transaction['date'],'%d.%m.%Y')==date:
            view_list.append(transaction)
    return view_list

def transaction_id_generator(transaction_list):
    transaction_id=1
    max_id=0
    if transaction_list==[]:
        return transaction_id
    
    for item in transaction_list:
        if "id" in item:
            if max_id<int(item["id"]):
                max_id=int(item["id"])
    return max_id+1

def delete_transaction(transaction_list: list, transaction_file):
    while True:
        try:
            choice=int(input("1.Continue\n2.Quite\n Your Choice: "))
        except ValueError:
            print("Invalid Choice")
            continue
        if choice==1:
            found=False
            try:
                transaction_id=int(input("Enter the Transaction ID you want to Delete: "))
            except ValueError:
                print("Invalid ID")
                continue
            for index, transaction in enumerate(transaction_list):
                if "id" in transaction:
                    if transaction["id"]==transaction_id:
                        found=True
                        del transaction_list[index]
                        print("Transaction Deleted Successfully")
                        save_database_after_deletion(transaction_list, transaction_file)
                        return
            if not found:
                print("Transaction does not exist, please confirm the Transaction ID from View Transaction")
        elif choice==2:
            return
        else:
            print("Invalid Choice")

def save_database_after_deletion(transaction_list: list,transaction_file):
    with open(transaction_file,"w") as trans_file:
        json.dump(transaction_list, trans_file, indent=4)
    


def main():
    transaction_file=Path(__file__).parent/"transaction_data.json"
    transaction_list=load_transaction(transaction_file)
    while True:
        user_choice=display_menu()
        #user_choice=5
        if user_choice==1:
            transact_type=get_transaction_type()
            date=get_transaction_date()
            transaction_id=transaction_id_generator(transaction_list)
            transaction=add_transaction(transact_type,date,transaction_id) #Saves Object of Class Transaction
            transaction_dict=transaction.to_dict() # uses instance method of class transaction to conver the user input data to dictionary
            save_transaction(transaction_dict,transaction_list,transaction_file)
            
        elif user_choice==2:
            view_transaction(transaction_list)      
        elif user_choice==3:
            summary_menu(transaction_list)        
        elif user_choice==4:
            filter_transaction(transaction_list)
        elif user_choice==5:
            delete_transaction(transaction_list,transaction_file)
        elif user_choice==6:
            print("Goodbye!!!")
            break
        else:
            print("Invalid menu option.")
    

if __name__=="__main__":
    main()
