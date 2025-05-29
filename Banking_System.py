# Banking Managemnet System- Made By Mahesh Raj Lamsal

from datetime import datetime
from tabulate import tabulate
# Empty List to Store Username and Password of user
users=[]
statement=[]

#Declaring User_Registration- Function
def register():
    manxe_ko_name_suruma=input("Create your username for bank account:- ").lower().strip()
    manxe_ko_pin=int(input("Enter your pin number for your bank account:- "))
    user={"name":manxe_ko_name_suruma,"id":manxe_ko_pin, "balance":  1000,}
    users.append(user)
    print(f"Account created successfully with the name of {manxe_ko_name_suruma}")

#Declaring User_Login using Function
def login():
    login_name=input("Enter your username: ")
    login_pin=int(input("Enter your pin number for your bank account:- "))
    for user in users:
        if user["name"]==login_name and user["id"]==login_pin:
            print(f"\n--- {user['name']} is logged in ---")
            user_menu(user)
            return

    print(" Invalid username or password")

#Exiting program
def exit():
    print("\nThank you for using Banking System")

# Displaying Operation-Banking
def user_menu(user):
   while True:
       print(" 1. To View Amount\n 2. To Deposit\n 3. To Withdraw\n 4. Logout\n 5. Statement\n")
       user_input_han=int(input("Enter your choice:- "))
       if user_input_han==1:
           print(f" Your Current Balance is NPR : {user['balance']}")
       elif user_input_han==2:
           naya_paisa=int(input("Enter the amount you want to deposit: "))
           purpose_deposit=input(" Purpose of Deposit: ")
           user["balance"]+=naya_paisa
           statement.append({
               'type': 'Deposit',
               'amount': naya_paisa,
               'purpose': purpose_deposit,
               'timestamp': datetime.now()
           })
           print(f"You Have Successfully Deposited NPR {naya_paisa} in your account.")
       elif user_input_han==3:
           kati_paisa=int(input("Enter the amount you want to withdrawal: "))
           withdrawl_purpose=input(" Purpose of Withdrawal: ")
           if user["balance"]>kati_paisa:
              user['balance']-=kati_paisa
              statement.append({
                  'type':'withdraw',
                  'amount':kati_paisa,
                  'purpose':withdrawl_purpose,
                  'timestamp': datetime.now()
              })
              print(f"You Have Successfully Withdrawn NPR {kati_paisa} from your account.")
           else:
               print("You don't have enough money")
       elif user_input_han==4:
           print("Thank you for using Banking System")
       elif user_input_han==5:
           print("--------------- STATEMENT--------------")
           rows = [[
               t['type'],
               t['amount'],
               t['purpose'],
               t['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
           ] for t in statement]

           # Print as a table
           print(tabulate(rows, headers=["Type", "Amount", "Purpose", "Date & Time"], tablefmt="grid"))

# Landing Main Interface
def main():
    while True:
        print("==================== Welcome to MAHESH-LAMSAL Banking System========================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        user_choice = int(input("Enter your choice:- "))
        if user_choice == 1:
            login()

        if user_choice == 2:
            register()

        if user_choice == 3:
            exit()
            break


main()
