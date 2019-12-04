import unittest
from app import model
import os

model.DBPATH = "_test.json"  # make sure your tests aren't messing up your real data

class TestAccount(unittest.TestCase):

    def setUp(self):
        # this code runs prior to every test case
        # it is important to know that test cases do not run in a predictable order
        # the purpose of setUp is to make sure assumptions are correct (data is in
        # the state you want it to be etc.)

        try:
            os.remove("_test.json")
        except FileNotFoundError:
            pass
    
    def test_creation(self):

        nobody = model.Account()
        self.assertIsNone(nobody.first_name, "default for first_name should be None")

        mike = model.Account(first_name="Mike", last_name="Bloom")
    
      def test_pin_creation(self):#TODO
          pass

    def test_save(self):
        mike = model.Account(first_name="Mike", last_name="Bloom", account_number="123456")
        mike.save()

        testmike = model.Account.from_account_number("123456")
        self.assertEqual(testmike.first_name, "Mike", "Saved account is loaded from file")
    
    # def test_login(self): #trying this one as well #TODO not a valid test -need to fix
    #     mike = model.Account(first_name="Mike", last_name="Bloom", account_number="123456", pin = "1234", balance=100.0)
        
    #     self.assertIn(mike.first_name, "Mike", "This account is in our records, it should login")

    def test_bad_login(self):#TODO need to set this up in controller/model
        pass
    
    def test_deposit(self):#I created this one
        mike = model.Account(account_number="123456", balance=100.0)

        mike.deposit(50.0)
        self.assertAlmostEqual(mike.balance, 150, "balance adds money")

        with self.assertRaises(ValueError, msg = "Negative Deposit should raise ValueError"):
            mike.deposit(-50.0)


    def test_withdraw(self):
        mike = model.Account(account_number="123456", balance=100.0)

        mike.withdraw(50.0)
        self.assertAlmostEqual(mike.balance, 50.0, "balance removes money")

        with self.assertRaises(model.InsufficientFundsError, msg="Overdraft should raise insufficient funds error"):  # note you don't need an 'as'
            mike.withdraw(10000.0)

  