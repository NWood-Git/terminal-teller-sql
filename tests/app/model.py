import json
import os

BASEDIR = os.path.dirname(__file__)
DBFILENAME = "accounts.json"
DBPATH = os.path.join(BASEDIR, DBFILENAME)

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
    
    def save(self):
        try:
            with open(DBPATH, "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}
        
        account_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "pin": self.pin,
            "balance": self.balance,
            "account_number": self.account_number
        }

        data[self.account_number] = account_data

        with open(DBPATH, "w") as json_file:
            json.dump(data, json_file, indent=2)


    @classmethod  # this is a decorator, decorators cause the following function to 
    # do something different than it normally would, they can do many kinds of things
    def from_account_number(cls, account_number):
        """ look for an entry with a given account number in accounts.json and return
        an instance of this class with its properties set if that account exists
        otherwise return None """
        with open(DBPATH, "r") as json_file:
            data = json.load(json_file)
        
        if account_number not in data:
            return None
        
        account_data = data[account_number]

        loaded_account = cls(**account_data)
            # cls(**account_data) means create an instance of this class with the
            # __init__ method, and take the dictionary account_data and treat it as a
            # set of argument=value, argument=value named arguments passed to the function
        
        return loaded_account
    
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
    
    def withdraw(self, amount): ###TODO - 3 - add Try/Except
        if not isinstance(amount, float):
            raise TypeError("Withdraw must be a float")
        if amount <= 0.0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Sorry you have insufficient funds for this transaction.")

        self.balance -= amount
        self.save()

### NW Trying to Make a new account number method is this what from_account_number is?

    
