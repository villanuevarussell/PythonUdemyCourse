#Class player which controls the players money
import Hand

class Player:
#initializes Player
	def __init__(self,name = "Player"):
		self.playername = name
		self.money = 100
		self.hand = Hand()

#Prints information about player
	def __str__(self):
		print(f"Player: {self.playername}")
		print(f"Money: ${self.money}")
		return ""

#returns string player name
	def name(self):
		return self.playername

#returns int money
	def money(self):
		return self.money

#mutator that adds to characters money
	def win(self,amount):
		self.money += amount
		print(f"{self.playername} wins {amount}!")
		print(f"New Balance: {self.money}")





if __name__ == "__main__":
	player1 = Player("Russell")
	print(player1)
	player1.win(150)
