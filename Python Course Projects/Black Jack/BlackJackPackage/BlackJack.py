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


#checks if 
def checkbust(player1,player2,bet):

		if player1.hand.value() > 21:
			print("Player Busted!")
			player1.lose(bet)
			clearhand(player1,player2)
			return True 

		elif player2.hand.value() > 21:
			print("Dealer Busted!")
			player1.win(bet)
			clearhand(player1,player2)
			return True

		else:
			return False

#Checks who wins game
def checkwin(player1,player2,bet):
	if player1.hand.value() > player2.hand.value():
		print("Player Wins!")
		player1.win(bet)
	elif player1.hand.value() < player2.hand.value():
		print("Dealer Wins!")
		player1.lose(bet)
	elif player1.hand.value() == player2.hand.value():
		print("Tied with Dealer!")



#Displays Board
def showboard(player1,player2):
	print("\n\n\nPlayer")
	print(player1.hand)
	print("\n\n\nDealer")
	print(player2.hand)
	print(f"\n\n\nYour score: {player1.hand.value()}")
	print(f"Dealer score: {player2.hand.value()}")	

#function for 1 round of Black Jack
def round(player1, player2,bet):
	player1.addcard(playdeck.deal())
	player2.addcard(playdeck.deal())
	player1.addcard(playdeck.deal())
#Dealers hidden card
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
	bust = checkbust(player1,player2, bet)

#Dealer turn
#adds hidden card to dealers hand
	if bust == False:
		player2.addcard(hiddencard)
		showboard(player1,player2)
		time.sleep(2)

	if bust == False:
		while player2.hand.value() < 21 and player2.hand.value() < 17:
			player2.addcard(playdeck.deal())
			showboard(player1,player2)
			bust = checkbust(player1,player2,bet)
			time.sleep(1)
		

	if bust == False:
		checkwin(player1,player2,bet)







#Black Jack Main
if __name__ == "__main__":

#initializes variables and shuffles deck object
	dealer = Player()
	playdeck = Deck()
	playdeck.shuffle()

	print("Welcome to Black Jack Game!\n \n \n")
	playername = input("Enter Player Name: ")

	user = Player(playername)

	replay = True
#loop to continuously repeat game
	while replay:
		clearhand(user,dealer)
		currentbet = bet(user)
		round(user,dealer,currentbet)


















