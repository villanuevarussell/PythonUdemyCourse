#Class the manages the game functions

#imports all classes related to game
import time
from Player import Player
from Hand import Hand
from Deck import Deck

def bet(player1):
	print(f"{player1.playername} has $ {player1.money}")
	while True:
		try:
#conditional statement if bet is greater than money	
			bet = int(input("How much would you like to bet?: "))
			if user.money >= bet:
				break	
			else:
				print("You do not have enough to bet!")	
		except:
			print("\nThat is not a valid bet!")
			print("Please Enter a numerical Value!")
			print(f"{user.playername} has $ {user.money}")
	return bet


#emptys both dealers
def clearhand(player1,player2):
	player1.hand.clear()
	player2.hand.clear()


#checks if any there is a bust
def checkbust(player1,player2,bet):

		if player1.hand.value() > 21:
			print("Player Busted!")
			player1.lose(bet)
			return True 

		elif player2.hand.value() > 21:
			print("Dealer Busted!")
			player1.win(bet)
			return True

		else:
			return False

#Checks who wins game
def checkwin(player1,player2,bet):
	time.sleep(3)
	if player1.hand.value() > player2.hand.value():
		print("Player Wins!")
		player1.win(bet)
	elif player1.hand.value() < player2.hand.value():
		print("Dealer Wins!")
		player1.lose(bet)
	elif player1.hand.value() == player2.hand.value():
		print("Tied with Dealer!\n")



#Displays Board
def showboard(player1,player2):
	print("\n\n\nBOARD:\n\n")
	print(f"\n\n{player1.playername}'s")
	print(player1.hand)
	print("\n\n\n")
	print("\n\n\nDealer's")
	print(player2.hand)
	print(f"\n\n\nYour score: {player1.hand.value()}")
	print(f"Dealer score: {player2.hand.value()}\n\n")	

#function for 1 round of Black Jack
def round(player1, player2,bet):
#Deals 4 cards out, 1 of dealers cards being hidden
	player1.addcard(playdeck.deal())
	player2.addcard(playdeck.deal())
	player1.addcard(playdeck.deal())
	hiddencard = playdeck.deal()


#user turn
	while player1.hand.value() < 21:
		while True:
			showboard(player1,player2)
			userinput = input ("Hit or Stay? (h or s): ")
			if userinput == 'h' or userinput == 'H' or userinput == 's' or userinput == 'S':
				break
			else:
				print("Please enter a valid input!")
#if the user hits it will add a card to player's hand
		if userinput == 'h' or userinput == 'H':
			player1.addcard(playdeck.deal())
			showboard(user,dealer)
		else:
			break

#returns false if User busts
	playerbust = checkbust(player1,player2, bet)

#Dealer turn
#adds hidden card to dealers hand
	if playerbust == False:
		player2.addcard(hiddencard)
		showboard(player1,player2)
		while player2.hand.value() < 21 and player2.hand.value() < 17:
			player2.addcard(playdeck.deal())
			showboard(player1,player2)
			time.sleep(3)
#After Dealer's turn, check if dealer busted
		dealerbust = checkbust(player1,player2,bet)	



#if Dealer does not bust check who wins
	if playerbust == False:
		checkwin(player1,player2,bet)







#Black Jack Main
if __name__ == "__main__":

#initializes variables and shuffles deck object
	dealer = Player()
	playdeck = Deck()
	playdeck.shuffle()

	print("Welcome to Black Jack Game!\n \n \n\n\n\n\n\n\n\n\n\n")
	playername = input("Enter Player Name: ")

	user = Player(playername)

#loop to continuously repeat game
	while user.money > 0:
		clearhand(user,dealer)
		currentbet = bet(user)
		round(user,dealer,currentbet)

		if playdeck.cardsleft() < 10:
			playdeck.newdeck()
			playdeck.shuffle()




















