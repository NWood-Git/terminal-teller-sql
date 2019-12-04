
def print_login_menu():
    print("""Welcome to Terminal Teller!:                                                       
                                                                                   
    1) create account                                                              
    2) log in                                                                      
    3) quit                                                                        
""")

def login_prompt():
    return input("Your choice:")

def bad_login_input():
    print("Input not recognized\n")

def goodbye():
    print("    Goodbye!\n")

def print_main_menu(user):
    #print(type(user))
    print(f"""Hello, {user.first_name} {user.last_name} ({user.account_number})                                                    
                                                                                
    1 Check balance                                                       
    2 Withdraw funds                                                           
    3 Deposit funds                                                            
    4 Sign out
""")

#NW added 11/21 - 11/22

def main_prompt():
    return input("Your choice:")

def input_first_name():
    return input("What is your first name? ")

def input_last_name():
    return input("What is your last name? ")

def input_new_pin():
    return input("Please input a 4-digit numeric pin for your account. ")

def bad_pin():
    print("The pin you have entered is invalid. Please try again.")

def inconsistent_pin():
    print("Those were not the same. Please try again. ")

def good_pin(pin):
    print(f'Your pin: {pin}, has been submitted.\nPlease save it.')

def new_acct_num(account_number):
    print(f"This is your account number: {account_number}, please save it somewhere safe.")

def invalid_credentials():
    print("Invalid credentials, please try again.")

def user_login_attempt():
    print("Please enter your credentials ")
    login_acct = input("Account Number: ")
    login_pin = input("Pin: ")
    return (login_acct, login_pin)

def goodbye():
    print('Thanks for using Terminal Teller. Have a great day!')

def show_balance(user):
    print(f"Your balance is: ${user.balance}")

def withdrawal_amount():
    amount = float(input("How much would you like to withdraw: "))
    return amount

def insufficient_funds():
    print("Sorry you have insufficient funds for this transaction.")

def not_positive():
    print("Sorry, you can't enter a negative number. the amount you entered needs to be positive!")

def post_withdrawal(amount, bal):
    print(f"You have withdrawn ${amount} your balance is now {bal}")

def deposit_amount():
    '''this is the deposit doc string'''
    amount = float(input("How much would you like to deposit: "))
    return amount

def post_deposit(amount, bal):
    print(f"You have deposited ${amount} your balance is now {bal}")