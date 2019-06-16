
if __name__ = "__main__":	
	replayGame = True
	while replayGame == True:

		print("Welcome to Tic Tac Toe!")

		#Condition for game loop
		gameOver = False


		#creates game board
		gameBoard = [0,1,2,3,4,5,6,7,8,9]
		player1 = None
		player2 = None

		choose_marker()


		#takes player 1 input, checks if player 1 wins, checks player 2 input, checks if player 2 wins
		while gameOver == False:
			player_input(gameBoard, player1)
			gameOver = win_check(gameBoard, player1)
			if gameOver == True:
				continue
			player_input(gameBoard, player2)
			gameOver = win_check(gameBoard, player2)
			if gameOver == True:
				continue

		#Does the user want to play again, has 
		replayGame = input("Do you want to play again? 'Y' or 'N': ")
		correctReplaySlection = False
		while correctReplaySlection == False:
			if replayGame == 'Y':
				correctReplaySlection = True
				break
			elif replayGame == 'N':
				correctReplaySlection = False
				break
			else:
				player1 = input("Please enter a valid selection. 'Y' or 'N': ")
		replayGame = replay()
		if replayGame == False:
			break








