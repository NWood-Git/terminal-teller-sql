import sqlite3
import os
import json #will remove later
from settings import DBPATH


class InsufficientFundsError(Exception):
    # create a new type of exception to check for with try & except
    pass


class Account:

    def __init__(self, **kwargs):
        self.account_number = kwargs.get("account_number") # if "account_number" is in kwargs, set self.account_number to that, otherwise set self.account_number to None
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.pin = kwargs.get("pin")
        self.balance = kwargs.get("balance", 0.0) # if you need a default value that is a mutable structure like a list or dict, you need to use a defaultdict from the collections module

        #print(kwargs)


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
    
    @classmethod
    def login(cls, account_number, pin):
        account = cls.from_account_number(account_number)
        if account is None:
            return None
        
        if account.pin != pin:
            return None
        
        return account
        
        
    def __repr__(self):
        """ this is Carter's generic repr method """
        classname = type(self).__name__  # this gives you the name of the class
        properties = self.__dict__  # self.properties are stored internally as a dictionary
        # you can get access to that dictionary with object.__dict__
        return f"<{classname} {properties}>"
    
    def deposit(self, amount):###TODO - 3 - add Try/Except
        if not isinstance(amount, float):
            raise TypeError("Deposit must be a float")
        if amount <= 0.0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.save()
    
    # def withdraw(self, amount): ###TODO - 3 - add Try/Except
    #     if not isinstance(amount, float):
    #         raise TypeError("Withdraw must be a float")
    #     if amount <= 0.0:
    #         raise ValueError("Withdraw must be positive")
    #     if amount > self.balance:
    #         raise InsufficientFundsError("Sorry you have insufficient funds for this transaction.")

    #     self.balance -= amount
    #     self.save()
    
    def add_new_acc_db(self):####class instance is a placeholder
            with sqlite3.connect(DBPATH) as connection:
                cursor = connection.cursor()
                sql_data = {"account_number" : self.account_number,
                            "first_name": self.first_name,
                            "last_name": self.last_name,
                            "pin": self.pin,
                            "balance" : self.balance}
                INSERT_SQL = """INSERT INTO accounts(account_number, first_name, last_name, pin, balance)
                            VALUES (:account_number, :first_name, :last_name, :pin, :balance);"""
                cursor.execute(INSERT_SQL, sql_data)
                #return cursor.lastrowid


    def withdraw(self, amount): ###TODO - 3 - add Try/Except ----In progress
        with sqlite3.connect(DBPATH) as connection:
            cursor = connection.cursor()
            #bal_sql = f"SELECT balance FROM accounts WHERE account_number={self.account_number}"
            cursor.execute(bal_sql)
        if not isinstance(amount, float):
            raise TypeError("Withdraw must be a float")
        elif amount <= 0.0:
            raise ValueError("Withdraw must be positive")
        elif amount > self.bal:
            raise InsufficientFundsError("Sorry you have insufficient funds for this transaction.")
        else:
            self.balance -= amount
        withdrawal = "UPDATE accounts SET balance={self.balance} WHERE account_number=?",(amount, self.account_number)
        cursor.execute(withdrawal)



    
