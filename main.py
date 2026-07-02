def add_transaction(transaction_type: str):
    amount=int(input("Enter amount:"))
    description=input("Enter description:")
    transaction_detail={"type":transaction_type,
                "amount":amount,
                "description":description
                }
    return transaction_detail

def save_transaction(transaction: dict,transaction_list: list):
    transaction_list.append(transaction)
    
    
def view_transaction(transaction_list: list):
    formatted_result=[]
    for transactions in transaction_list:
        transaction_type=transactions['type']
        amount=transactions['amount']
        description=transactions['description']
        formatted_result.append(f"Transaction Type:{transaction_type} Amount:{amount} Description:{description}")
    return formatted_result

    

def display_menu():
    print(("\n===== Personal Finance Manager ====="))
    user_choice=int(input("1.Add Income\n2.Add Spends\n3.View Transaction\n4.Exit\nYour Choice: "))
    return user_choice
    


def main():
    transaction_list=[]
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
            print("Goodbye!")
            break
        else:
            print("Invalid menu option.")
        
        if user_choice in(1,2):
            transaction=add_transaction(transact_typ)
            save_transaction(transaction,transaction_list)
    
    #transaction_list=[{'type': 'Income', 'amount': 500, 'description': 'abc'}, {'type': 'Expense', 'amount': 433, 'description': 'dsa'}]
    #formatted=view_transaction(transaction_list)
    #for item in formatted:
        #print(item)
    #    if formatted!=[]:
    #        print(item)
        
    #print("No Transactions to show.") 

if __name__=="__main__":
    main()
