from app import view   # imports from module folders are relative to the file being executed by python3 since main.py is at the top level, imports need to come from app. even for the files inside of app
from app import model
from random import randint
import sqlite3
from settings import DBPATH

### The below 6-7 todo's were input on 11/22/2019 ~6:30PM and have not been completed
###TODO - 1 - fix loop - after withhdrawal / desposit it loops to first menu. Check balance loops to user menu.
###TODO - 1B - Sign Out should give goodbye not sent you back to main menu. 
###TODO - 2 - does not disply insuffient funds error
###TODO - 3 - add Try / Except to deposit / withdrawal errors -In Controller not model
###TODO - 4 - invalid credentials error
###TODO - 5 - after creating account it loops back to 1st TT menu - should go to login menu or have you sign in

def run():
    while True:
        user_account = login_menu()  # returns the logged in user or None for quit
        if user_account == None:  # login menu returns None if 'quit' is selected
            view.goodbye()
            break
        main_menu(user_account) # when the user exits the main menu they will go back to login

def login_menu():
    while True:
        view.print_login_menu()
        choice = view.login_prompt().strip()
        if choice not in ("1", "2", "3"):
            view.bad_login_input()
        elif choice == "3":
            #view.goodbye()
            return None # return None for quit

        elif choice == "1": #choice 1 = create account #NW added the below code in choice 1
            """ DONE in create_account() function: prompt for firstname, lastname, and pin, and confirm pin
            create the account and then tell the user what their new account number is """
            create_account()
            pass

        elif choice == "2": #choice 2 is login
            """ TODO: prompt functions to ask for account and PIN, use try, except
            to check for bad login """
            account = login_attempt()
            if account:
                return account 
            else:
                pass ###TODO - 4- here for invald credentials error

# def create_account(): #SUCESSFULL UPDATED for SQL ###TODO - make sure this adds a class 12/3/2019 ~8PM
#     """ call this from the main login loop """
#     account_number = new_acct_num()
#     print(account_number) #testing line
#     first_name = view.input_first_name() 
#     last_name = view.input_last_name()
#     pin = new_cust_pin()
#     print(pin) #testing line
#     balance = 0
#     with sqlite3.connect(DBPATH) as connection:
#         cursor = connection.cursor()
#         sql_data = {"account_number" : account_number,
#                     "first_name": first_name,
#                     "last_name": last_name,
#                     "pin": pin,
#                     "balance" : balance}
#         INSERT_SQL = """INSERT INTO accounts(account_number, first_name, last_name, pin, balance)
#                     VALUES (:account_number, :first_name, :last_name, :pin, :balance);"""
#         cursor.execute(INSERT_SQL, sql_data)
#         #return cursor.lastrowid

def create_account():
    """ call this from the main login loop """
    account_number = new_acct_num()
    print(account_number) #testing line
    first_name = view.input_first_name() 
    last_name = view.input_last_name()
    pin = new_cust_pin()
    print(pin) #testing line
    balance = 0
    new_acc_obj = model.Account(account_number=account_number, first_name=first_name, last_name=last_name, pin=pin, balance=0) # is this correct? OR Redundant?
    new_acc_obj.add_new_acc_db()

def login_attempt(): ## TODO: is this done?
    """ call this from the main login loop """
    #FIXME - add invalid login error
    while True:
        account_number, pin = view.user_login_attempt()
        account = model.Account.login(account_number, pin)
        #print(account.account_number)
        return account   

def main_menu(user): #TODO: Complete this function
    while True:
        view.print_main_menu(user)
        choice = view.main_prompt()
        """ TODO: add bad input message """
        if choice == "1":#1 is check balance
            view.show_balance(user) ###TODO - 1 - Currently brings you to user menu - add Would you like to do anything else? Y (main user menu) / N (quit / goodbye)
        elif choice == "2":#2 is Withdraw Funds
            amount = view.withdrawal_amount()
            try:
                user.withdraw(amount) #funct is in model
                view.post_withdrawal(amount, user.balance)  ###TODO - 1 -same as above. Note with the break it brings you back to 1st menu (not user)
            except ValueError:
                view.not_positive()#print("The amount must be positive") #move the print to views
            except model.InsufficientFundsError:
                view.insufficient_funds()
            #break
        elif choice == "3":
            amount = view.deposit_amount()
            user.deposit(amount) #funct is in model
            view.post_deposit(amount, user.balance) ###TODO - 1 -same as above. Note with the break it brings you back to 1st menu (not user)
            #break                    
        elif choice == "4": #4 is sign out - ###TODO - 1B - give goodbye message not bring you back to 1st menu
            break


def new_acct_num(override = None): ##Successfully updated to check if account number generated is already in use and give a new one.
    if override is not None:
        return override
    while True:
        account_number = randint(100000,999999) ##randint(1,3) for test and put 1 & 2 ub the that in dict.
        with sqlite3.connect(DBPATH) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM accounts WHERE account_number={account_number};")
            x = cursor.fetchone()
            if x == None:
                return account_number
            #else:#for test
            #    return x#for test



def new_cust_pin(): #this goes in model or controller? It talks with views - also should this be created outside of create_account and called
    '''call this in the create account fuction'''
    new_pin = '0'
    while True:
        new_pin = view.input_new_pin()
        if len(new_pin) != 4 or new_pin.isnumeric() == False:
            view.bad_pin()
        else:
            confirm_pin = input("Please re-enter your pin to confirm. ")
            if new_pin == confirm_pin:
                pin = new_pin
                view.good_pin(pin)
                return pin                
            else:
                view.inconsistent_pin()


run()