from IPython.display import clear_output

#Function to Show Board
def display_board(board):
    print(f"     |   |   ")
    print(f"   {board[7]} | {board[8]} | {board[9]} ")
    print(f"     |   |  ")
    print('---------------')
    print(f"     |   |   ")
    print(f"   {board[4]} | {board[5]} | {board[6]} ")
    print(f"     |   |  ")
    print('---------------')
    print(f"     |   |   ")
    print(f"   {board[1]} | {board[2]} | {board[3]} ")
    print(f"     |   |  ")
    pass

#function for user to select a marker
def choose_marker():
    #Condition for correct Selection
    correctSelection = False

    #uses global player 1 and 2 variables
    global player1
    global player2

    #choose marker for first player, while loop forces user to choose a correct selection
    player1 = input("Please pick a marker 'X' or 'O': ")
    while correctSelection == False:
        if player1 == 'X' or player1 == 'O':
            correctSelection = True
            break
        else:
            player1 = input("Please enter a valid selection. 'X' or 'O': ")

    #Second player gets remaining option
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 ='X'


def player_input(board,player):
    #selection flag to ensure user makes a correct selection and that it has not been selected yet 
    correctSelection = False
    display_board(board)
    playerSelection = int (input(f"{player} Please select a number 1-9 that is not yet selected: "))

    #runs through specific conditions to check if it is a valid input
    while correctSelection == False:
        #ensure number is greater than 0 and less than 10
        if playerSelection >= 10 or playerSelection == 0:
            display_board(board)
            print("That number is out of range")
            playerSelection = int (input(f"{player} Please select a number 1-9 that is not yet selected: "))
        #ensures that the selection has not been selected yet
        elif board[playerSelection] == 'X' or board[playerSelection] == 'O':
            display_board(board)
            print("That number has been selected")
            playerSelection = int (input(f"{player} Please select a number 1-9 that is not yet selected: ")) 
        #allows changes to the board
        else:
            board[playerSelection] = player
            correctSelection == True
            break

#function to check if there is a winner
def win_check(board, player):
    #count is number to check if all the spots have been used
    count = 0
    #loops through entire board to check if all the spots have been taken, count is added if spot is taken
    for position in range(len(board)):
        if board[position] == 'X' or board[position] == 'O':
            count += 1
    #if there are 9 spots taken then the game is a draw
    if count == 9:
        print("Game is a draw!")
        return True

        
    #if any of these conditions are true, the player wins
    if (board[1] == player and board[2] == player and board[3] == player) or (board[4] == player and board[5] == player and board[6] == player) or (board[7] == player and board[8] == player and board[9] == player) or (board[1] == player and board[4] == player and board[7] == player)  or (board[2] == player and board[5] == player and board[8] == player)  or (board[3] == player and board[6] == player and board[9] == player)  or (board[3] == player and board[5] == player and board[7] == player) or (board[1] == player and board[5] == player and board[9] == player) :
        print(f"Player {player} wins!")
        return True
    else:
        return False
        

#asks user if they want to play again
def replay():
    correctReplaySlection = False
    while correctReplaySlection == False:
        if replayGame == 'Y':
            correctReplaySlection = True
            return True          
        elif replayGame == 'N':
            return False
        else:
            print("Do you want to play again?")
            player1 = input("Please enter a valid selection. 'Y' or 'N': ")

if __name__ == "__main__":
    test_board = ['#',1,2,3,4,5,6,7,8,9]
    display_board(test_board)

    player1 = 'X'
    player_input(player1,test_board)


