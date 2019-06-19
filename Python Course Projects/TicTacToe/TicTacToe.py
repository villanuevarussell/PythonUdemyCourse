from TicTacToePackage import TicTacToeFunctionDefinitions



if __name__ == "__main__":	
	replayGame = True
	while replayGame == True:

		print("Welcome to Tic Tac Toe!")

		#Condition for game loop
		gameOver = False

		#creates game board
		gameBoard = [0,1,2,3,4,5,6,7,8,9]

		#function that creates a tuple to represent each player
		players = TicTacToeFunctionDefinitions.choose_marker()
		print(players)


		#takes player 1 input, checks if player 1 wins, checks player 2 input, checks if player 2 wins
		while gameOver == False:
			TicTacToeFunctionDefinitions.player_input(gameBoard, players[0])
			gameOver = TicTacToeFunctionDefinitions.win_check(gameBoard, players[0])
			if gameOver == True:
				continue
			TicTacToeFunctionDefinitions.player_input(gameBoard, players[1])
			gameOver = TicTacToeFunctionDefinitions.win_check(gameBoard, players[1])
			if gameOver == True:
				continue
		replayGame = TicTacToeFunctionDefinitions.replay()
		
	








