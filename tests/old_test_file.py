import os
from app.model import Account, InsufficientFundsError

# print(__file__)
# print(os.path.dirname(__file__))
# basepath = os.path.dirname(__file__)
# databasename = "accounts.json"
# datapath = os.path.join(basepath, databasename)
# print(datapath)

# first = Account()
# print(first.account_number)
second = Account(account_number="1234", pin="1234", balance=3.5, first_name="Jack")
# print(second.account_number)
second.save()
# third = Account(a=1, b=2, c=3, d=None)

mike = Account(balance=1.0)
try:
    mike.withdraw(2.0)
except InsufficientFundsError:
    print("withdraw error works correctly")

mike.account_number = "00001"
mike.pin = "0000"
mike.save()

mike_reloaded = Account.login("00001", "0000")
print(mike_reloaded)
assert mike_reloaded.balance == 1.0, "mike has the right data"