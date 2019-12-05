#Removed from model on 12/4/2019@ 7:00- 9:40PM


    # @classmethod# this is a decorator, decorators cause the following function to 
    # # do something different than it normally would, they can do many kinds of things
    # def from_account_number(cls, account_number):
    #     """ look for an entry with a given account number in accounts.json and return
    #     an instance of this class with its properties set if that account exists
    #     otherwise return None """
    #     
    #     with sqlite3,connect(DPATH) as connection:
    #         cursor = connection.cursor()
    #         cursor.execute(f"SELECT * FROM accouts WHERE account={self.account}")
    #         acc_check = cursor.fetchone()
    #     # with open(DBPATH, "r") as json_file:
    #     # #     data = json.load(json_file)
        
    #         if acc_check == None:
    #             return None
            
    #         account_data = self #data[account_number]

    #         loaded_account = cls(**account_data)
    #             # cls(**account_data) means create an instance of this class with the
    #             # __init__ method, and take the dictionary account_data and treat it as a
    #             # set of argument=value, argument=value named arguments passed to the function
        
    #     return loaded_account

    # def withdraw(self, amount): ###TODO - 3 - add Try/Except ----In progress
    #     with sqlite3.connect(DBPATH) as connection:
    #         cursor = connection.cursor()
    #         bal_sql = f"SELECT balance FROM accounts WHERE account_number={self.account_number}"
    #         bal = cursor.execute(bal_sql)
    #     if not isinstance(amount, float):
    #         raise TypeError("Withdraw must be a float")
    #     elif amount <= 0.0:
    #         raise ValueError("Withdraw must be positive")
    #     elif amount > bal:
    #         raise InsufficientFundsError("Sorry you have insufficient funds for this transaction.")
    #     else:
    #         print(bal)
        #     self.balance -= amount
        # withdrawal = "UPDATE accounts SET balance={self.balance} WHERE account_number=?",(amount, self.account_number)
        # cursor.execute(withdrawal)
    
    # def save(self):# Will be removed 
    #     try:
    #         with open(DBPATH, "r") as json_file:
    #             data = json.load(json_file)
    #     except FileNotFoundError:
    #         data = {}
        
    #     account_data = {
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #         "pin": self.pin,
    #         "balance": self.balance,
    #         "account_number": self.account_number
    #     }

    #     data[self.account_number] = account_data

    #     with open(DBPATH, "w") as json_file:
    #         json.dump(data, json_file, indent=2)

    ###Removed from controller 12/4/2019 @ 7:50PM
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


