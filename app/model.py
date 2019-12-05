import sqlite3
import os
from settings import DBPATH


class InsufficientFundsError(Exception):
    # create a new type of exception to check for with try & except
    pass


class Account:
    tablename = 'accounts'

    def __init__(self, **kwargs):
        self.id =kwargs.get('id')
        self.account_number = kwargs.get("account_number") # if "account_number" is in kwargs, set self.account_number to that, otherwise set self.account_number to None
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.pin = kwargs.get("pin")
        self.balance = kwargs.get("balance", 0.0) # if you need a default value that is a mutable structure like a list or dict, you need to use a defaultdict from the collections module

        #print(kwargs)


    @classmethod
    def login(cls, account_number, pin):
        with sqlite3.connect(DBPATH) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
        SQL = f"SELECT * FROM {cls.tablename} WHERE account_number=:account_number AND pin=:pin;"
        cursor.execute(SQL,{'account_number':account_number, 'pin':pin})
        row = cursor.fetchone()
        if row is None:
            return None
        d_row = dict(row)
        loaded_account = cls(**d_row)
        return loaded_account
        
        
    def __repr__(self):
        """ this is Carter's generic repr method """
        classname = type(self).__name__  # this gives you the name of the class
        properties = self.__dict__  # self.properties are stored internally as a dictionary
        # you can get access to that dictionary with object.__dict__
        return f"<{classname} {properties}>"


    def add_new_acc_db(self):####class instance is a placeholder
            with sqlite3.connect(DBPATH) as connection:
                cursor = connection.cursor()
                sql_data = {"account_number" : self.account_number,
                            "first_name": self.first_name,
                            "last_name": self.last_name,
                            "pin": self.pin,
                            "balance" : self.balance}
                self.save()
                # INSERT_SQL = """INSERT INTO accounts(account_number, first_name, last_name, pin, balance)
                #             VALUES (:account_number, :first_name, :last_name, :pin, :balance);"""
                # cursor.execute(INSERT_SQL, sql_data)
                #return cursor.lastrowid


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
    

    def save(self):
        if self.id is None:
            # if self.id has not been set, then we assume the object does not
            # yet have a saved row in the database so we will be calling an
            # insert statement.
            # after which, we will set self.id to the primary key of the new row
            self.insert()
        else:
            self.update()

    def update(self):
        SQL = f"UPDATE {self.tablename} SET balance= :balance WHERE id=:id;"
        with sqlite3.connect(DBPATH) as connection:
            cursor = connection.cursor()
            cursor.execute(SQL,{'id' : self.id, 'balance' : self.balance})

    def insert(self):
        SQL = f"INSERT INTO {self.tablename}(account_number, first_name, last_name, pin, balance) VALUES(:account_number, :first_name, :last_name, :pin, :balance);"
        with sqlite3.connect(DBPATH) as connection:
            cursor = connection.cursor()
            cursor.execute(SQL,{"account_number":self.account_number, "first_name":self.first_name, "last_name":self.last_name, "pin":self.pin, "balance":self.balance})
            