from IPython.display import clear_output

#displays board
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

def player_input(player,board):
    #try catch statement to force user to select a correct selection
    display_board(board)
    while True:
        try:
            playerSelection = int (input(f"{player} Please select a number 1-9 that is not yet selected: "))
            if playerSelection >= 10 or playerSelection == 0:
                display_board(board)
                print("That number is out of range")
                continue
            elif board[playerSelection] == 'X' or board[playerSelection] == 'O':
                display_board(board)
                print("That number has been selected")
                continue
        except:
            display_board(board)
            print("That is not an integer!")
        else:
            board[playerSelection] = player
            break
            

if __name__ == "__main__":
    test_board = ['#',1,2,3,4,5,6,7,8,9]
    display_board(test_board)

    player1 = 'X'
    player_input(player1,test_board)


