#Class player which controls the players money
from Hand import Hand
import Card

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
		print(self.hand)
		return ""


	def addcard(self,card):
		self.hand.add(card)

	def name(self):
		return self.playername

	def money(self):
		return self.money


#mutator that adds to characters money
	def win(self,amount):
		self.money += amount
		print(f"\n{self.playername} wins {amount}!")
		print(f"New Balance: {self.money}\n")

	def lose(self,amount):
		self.money -= amount
		print(f"\n{self.playername} loses {amount}!")
		print(f"New Balance: {self.money}\n")





if __name__ == "__main__":
	player1 = Player("Russell")
	player1.addcard(Card.Card(suit = "Diamonds", rank = "Two"))
	player1.addcard(Card.Card(suit = "Clovers", rank = "Nine"))
	player1.addcard(Card.Card(suit = "Clovers", rank = "Ace"))

	print(player1)
	player1.win(150)
	print(player1.name())
	x = player1.money
	print(x)
	print(player1.hand.value())







