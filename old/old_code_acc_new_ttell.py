def acct_num():
    while True:
        account_number = input("Please input a 6 digit account number: ")
        if account_number.isnumeric() == False or len(account_number) != 6:
            bad_acct_msg()
        elif account_number in new_customer_dict:
            in_use_account() #do we link this to te login function?
            break
        else:
            good_acct_msg(account_number)
            new_customer_dict[account_number] = account_number 
            return account_number

new_customer_dict = {} 
account_number = None


def new_cust_name(account_number):
    first_name = input("Please tell us your first name. ")
    last_name = input("Please input your last name. ")
    new_customer_dict['First Name'] = first_name 
    new_customer_dict[account_number] = {'First Name': first_name , 'Last Name' : last_name, 'Pin' : None, 'Balance' : 0} #note balance defaults to 0
    new_customer_dict[account_number] = {'First Name': first_name , 'Last Name' : last_name, 'Pin' : None, 'Balance' : 0} #note balance defaults to 0
    new_customer_dict[account_number] = {'First Name': first_name , 'Last Name' : last_name, 'Pin' : None, 'Balance' : 0} #note balance defaults to 0
    new_customer_dict[account_number] = {'First Name': first_name , 'Last Name' : last_name, 'Pin' : None, 'Balance' : 0} #note balance defaults to 0
    new_customer_dict[account_number] = {'First Name': first_name , 'Last Name' : last_name, 'Pin' : None, 'Balance' : 0} #note balance defaults to 0

def new_cust_pin(account_number):
    pin = input("Please input a 4-digit numeric pin for your account. ")
    while True:
        if len(pin) != 4 or pin.isnumeric() == False:
            bad_pin()
            break
        else:
            new_customer_dict[account_number]['Pin'] = pin
            break

def user_choice():
    user_choice = input("Make a selection: ")
    return user_choice

def invalid_selection():
    print("Your selection was invalid. Please try again.")

def bad_acct_msg():
    print('Your account number is invalid. It must be 6 numeric characters long. Try Again')

def good_acct_msg(account_number):
    print(f"Your account number {account_number} is valid.")

def in_use_account():
    print("This account number is already in our records, please log in. ")

def bad_pin():
    print("The pin you have entered is invalid. Please try again.")

acct_num()
new_cust_name(account_number)
new_cust_pin(account_number)