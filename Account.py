"""An account file for our Simple bank."""

class Account:
   """An Account class that stores account info"""

   def __init__(self, balance, account_type="checking"):
      self.balance = balance
      self.account_type = account_type

   def deposit(self, money):
      self.balance += money
      return self.balance

   def withdraw(self, money):
      if self.balance < money:
         print("You do not have enough in your account to withdaw ${0:,.2f}. Your current balance is {1}"
            .format(money, self.print_balance()))
      else:
         self.balance -= money
      return self.balance

   def check_balance(self):
      return self.balance

   def print_balance(self):
      return '${:,.2f}'.format(self.balance)

   def interest(self, percentage):
      """A function that applies the passed interest to the account."""
      self.balance *= percentage


class Person:
   """A class that tracks individual Persons in our bank."""

   def __init__(self, first_name, last_name, email):
      self.accounts = {}
      self.first_name = first_name
      self.last_name = last_name
      self.email = email

   def open_account(self, initial_balance, account_name, account_type="checking"):
      new_account = Account(initial_balance, account_type)
      self.accounts[account_name] = new_account

   def deposit(self, money, account_name):
      new_amount = self.accounts[account_name].deposit(money)
      print("${0:,.2f} was successfully deposited to {1}".format(money, account_name))

   def withdraw(self, money, account_name):
      new_amount = self.accounts[account_name].withdraw(money)
      print("${0:,.2f} was successfully withdrawn to {1}".format(money, account_name))

   def close_account(self, account_name):
      del self.accounts[account_name]

   def show_accounts(self):
      """Display on the screen all of a user's account info."""
      print("Accounts >>> Balance")
      print("-----------------------------")
      for k,v in self.accounts.items():
         print(k, ">>>", v.print_balance())
      print("\n\n\n")

class Bank:

   def __init__(self):
      self.customers = {}
      self.savings_interest = 1.07

   def new_customer(self, first_name, last_name, email):
      new_customer = Person(first_name, last_name, email)
      customers[email] = new_customer

   def remove_customer(self, email):
      del self.customers[email]

   def show_customer_info(self, email):
      pass

   def customer_deposit(self, email, money, account_name):
      pass

   def customer_withdraw(self, email, money, account_name):
      pass

   def make_customer_account(self, email, money, account_name):
      pass

   def remove_customer_account(self, email, account_name):
      pass



# test = Person("Tiffany","Ralph","TheTeacherTAR@gmail.com")
# test.open_account(100,"Trustfund")
# test.deposit(100, "Trustfund")
# test.open_account(540, "Savings", "savings")
# test.withdraw(50, "Savings")
# test.show_accounts()
# test.close_account("Savings")
# test.show_accounts()

#test = Account(100,"Tiffany")
#print(test.print_balance())
#test.deposit(50)
#print(test.print_balance())
#test.withdraw(75)
#print(test.print_balance())
#test.withdraw(100)
#print(test.print_balance())
#test.interest(1.07)
#print(test.print_balance())
