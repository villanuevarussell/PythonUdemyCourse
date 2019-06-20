#Class the manages the game functions

#imports all clases related to game from specified modules
import time
import sys
from Player import Player
from Hand import Hand
from Deck import Deck

#function that takes user input for betting
def bet(player):
	print(f"{player.playername} has $ {player.money}")	
	while True:
		#Try Except statement if user inputs something other than a number
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
			print(f"{player.playername} has $ {player.money}")
	return bet

#asks user if they want to play again
def replay():
    while True:
        replaygame = input("Do you want to continue playing? (Type 'Y' or 'N'): ")
        if replaygame == 'y' or replaygame == 'Y':
            return True
        elif replaygame == 'n' or replaygame == 'N':
            sys.exit("Game Ended!")
        else:
            print("Invalid Selection!")


#clears the hand of both Player Objects
def clearhand(player1,player2):
	player1.hand.clear()
	player2.hand.clear()


#function for 1 round of Black Jack
def round(player1, player2,bet):
#Function defintions for functions that will be used in one round of Black Jack
	#Displays Board
	def showboard(player1,player2,DealerTurn):
	#Conditional Statement for showing the Dealer Hand with a hidden card if DealerTurn == False
		if DealerTurn == False:
			print("\n\n\nBOARD:\n\n")
			print(f"\n\n{player1.playername}'s")
			print(player1.hand)
			print("\n\n\n")
			print("\n\n\nDealer's")
			print(player2.hand)
			print("Hidden Card")
			print(f"\n\n\nYour score: {player1.hand.value()}")
			print(f"Dealer score: {player2.hand.value()}\n\n")
		else:
			print("\n\n\nBOARD:\n\n")
			print(f"\n\n{player1.playername}'s")
			print(player1.hand)
			print("\n\n\n")
			print("\n\n\nDealer's")
			print(player2.hand)
			print(f"\n\n\nYour score: {player1.hand.value()}")
			print(f"Dealer score: {player2.hand.value()}\n\n")			

	#checks if Player1 or Player2 busts
	def checkbust(player1,player2,bet):
			if player1.hand.value() > 21:
				print("Player Busted!")
				player1.lose(bet)
				return True

			if player2.hand.value() > 21:
				print("Dealer Busted!")
				player1.win(bet)
				return True 


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
			print("Tied with Dealer!")
			print("Bet returned!\n")

#Deals 4 cards out, 1 of dealers cards being hidden
	player1.addcard(playdeck.deal())
	player2.addcard(playdeck.deal())
	player1.addcard(playdeck.deal())
	hiddencard = playdeck.deal()
	DealerTurn = False


#user turn
	while player1.hand.value() < 21:
		while True:
			showboard(player1,player2,DealerTurn)
			userinput = input ("Hit or Stay? (h or s): ")
			if userinput == 'h' or userinput == 'H' or userinput == 's' or userinput == 'S':
				break
			else:
				print("Please enter a valid input!")
#if the user hits it will add a card to player's hand
		if userinput == 'h' or userinput == 'H':
			player1.addcard(playdeck.deal())
			showboard(user,dealer,DealerTurn)
		else:
			break

#returns false if User busts
	playerbust = checkbust(player1,player2, bet)

	#initialized to be used in if statement
	dealerbust = None
	#used for using second option on display
	DealerTurn = True
#Dealer turn
#adds hidden card to dealers hand
	if playerbust == False:
		player2.addcard(hiddencard)
		showboard(player1,player2,DealerTurn)
		while player2.hand.value() < 21 and player2.hand.value() < 17:
			time.sleep(2)
			player2.addcard(playdeck.deal())
			showboard(player1,player2,DealerTurn)

#After Dealer's turn, check if dealer busted
		dealerbust = checkbust(player1,player2,bet)	

#if Dealer does not bust check who wins
	if dealerbust == False:
		checkwin(player1,player2,bet)


#Black Jack Main
if __name__ == "__main__":

	#initializes variables and shuffles deck object
	dealer = Player()
	playdeck = Deck()
	playdeck.shuffle()

	print("Welcome to Black Jack Game!\n \n \n\n\n\n\n\n\n\n\n\n")
	playername = input("Enter Player Name: ")

	#initializes Player Class
	user = Player(playername)
	replayGame = True

#loop to continuously repeat game until user has no more money
	while user.money > 0 and replay:
		#has user enter a bet
		currentbet = bet(user)
		#plays one round of black jack
		round(user,dealer,currentbet)
		replayGame = replay()
		#clears hand
		clearhand(user,dealer)

		if playdeck.cardsleft() < 10:
			playdeck = Deck()
			playdeck.shuffle()




















