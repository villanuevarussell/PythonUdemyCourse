#Deck Class
import random

#card class to hold attributes of the card
class Card:
	values = {"2":2 , "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8 , "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King": 10, "Ace":11}	
	
	def __init__(self,suit = "Hearts", rank = "Ace"):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		return f"{self.rank} of {self.suit}"

	def value(self):
		return self.values[self.rank]




if __name__ == "__main__":
	card = Card()
	print(card)
	print(card.value())

