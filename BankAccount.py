
class BankAccount:
  """docstring for ClassName"""
  def __init__(self, amount = 0):
    # super(ClassName, self).__init__()
    self.balance = amount

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount > self.balance:
      return "invalid transaction"

    self.balance -= amount
    return self.balance


class MinimumBalanceAccount(BankAccount):
  pass
    

a = BankAccount(90)
print "Balance: ",a.balance
print "depociting: ",a.deposit(200)
print "withdrawing: ",a.withdraw(20)
print "balance from withdrawing: ",a.balance

b = MinimumBalanceAccount(90)
print "b: ",b.balance