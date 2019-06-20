#import Card class to add to list to create a deck of cards
from Card import Card
#import random to use shuffle function
import random

#Class that creates a deck of cards (List of Card Objects)
class Deck:
	suits = ("Hearts","Diamonds","Spades","Clovers")
	ranks = ("Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King")
	deck = []

#creates a list of deck with objects card
	def __init__(self):	
#for loop create list of Card objects to represent cards
		for suit in range(len(self.suits)):
			for rank in range(len(self.ranks)):
				self.deck.append(Card(suit = self.suits[suit],rank = self.ranks[rank]))

#prints out cards in the deck
	def __str__(self):
		for card in range(len(self.deck)):
			print(self.deck[card])
		return ("")

#shuffles deck
	def shuffle(self):
		random.shuffle(self.deck)
		print("Deck Shuffled!")

#Deals a card object out
	def deal(self):
		if len(self.deck) == 0:
			print("Can not deal, no more cards left")
		return self.deck.pop()

#returns 
	def cardsleft(self):
		return len(self.deck)



#tests functions 
if __name__ == "__main__":
	deck = Deck()
	print(deck)
	deck.shuffle()
	print(deck)
	card = deck.deal()
	print("")
	print(card)
	print("")
	print(deck)
	print(deck.cardsleft())








