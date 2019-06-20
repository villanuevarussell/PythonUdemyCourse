#Class to hold Card Objects

#uses Card objects in Hand
from Card import Card

class Hand:

#initializes list of card objects
	def __init__(self):
		self.cards = []

#prints out list of card objects (Hand)
	def __str__(self):
		if len(self.cards) == 0:
			print("No Cards in hand!")
		else:
			print("Hand:")
			for i in range(len(self.cards)):
				print(self.cards[i])
		return ""


#add a card to hand
	def add(self, card):
		self.cards.append(card)

#remove all cards from hand
	def clear(self):
		self.cards = []

#returns users hand value
	def value(self):
		Ace = 0
		total = 0

		for numberofcards in range(len(self.cards)):
			total += self.cards[numberofcards].value()
			if self.cards[numberofcards].rank == "Ace":
				Ace += 1
			else:
				continue

#conditional statement to control if there are multiple Aces
		while True:
			if total > 21 and Ace > 0:
				total -= 10
				Ace -=1
			else:
				break

		return total


#tests functions in hand
if __name__ == "__main__":
	playerhand = Hand()
	playerhand.add(Card(suit = "Hearts", rank = "Ace"))
	playerhand.add(Card(suit = "Diamonds", rank = "Nine"))
	playerhand.add(Card(suit = "Clovers", rank = "Nine"))
	playerhand.add(Card(suit = "Clovers", rank = "Ace"))
	playerhand.add(Card(suit = "Clovers", rank = "Ace"))

	print(playerhand)
	print(playerhand.value())
	playerhand.clear()
	print(playerhand)





