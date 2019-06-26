class Account():
	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f"Owner:   {self.owner}\nBalance: ${self.balance}"

	def deposit(self,amount):
		self.balance += amount
		print("Deposit Accepted")

	def withdraw(self,amount):
		if amount > self.balance:
			print("Funds Unavailable!")
		else:
			self.balance -= amount
			print("Withdrawal Accepted")

 


acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.withdraw(20)
acct1.deposit(5)
acct1.withdraw(120)




