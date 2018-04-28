class BankAccount(object):
 balance=0
 def __init__(self,name):
    self.name=name
 def __repr__(self):
    return "Account Holder: %s, Account Balance: $%.2f" % (self.name,self.balance)
 def show_balance(self):
    print("Account Balance: $%.2f"%(self.balance))
 def deposit(self,amount):
     self.amount=amount
     if self.amount<=0:
         print("Deposit amount should larger than 0")
         return
     else:
         print("The amount of deposit you entered is : $%.2f" %(self.amount))
         self.balance += self.amount
         self.show_balance()
 def withdraw(self,amount):
      self.amount=amount
      if self.amount>self.balance:
         print("You cannot withdraw more than you have.")
         return
      else:
         print("You are withdrawing %.2f"%(self.amount))
         self.balance-=self.amount
         self.show_balance()
my_account=BankAccount("Huangyining")
print (my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
