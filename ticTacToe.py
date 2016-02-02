theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])         #prints the board
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
  

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or #checking across top row
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or #checking across middle row
            (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or #checking across bottom row
            (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or #checking vertically on left row
            (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or #checking vertically the middle row
            (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or #checking vertically the right row
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or #checking diagonally
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))   #checking diagonally

    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)                                       #prints the board before every turn
        print('Turn for ' + turn + '. Move on which space?')    #asks player which space they choose
        move = input()                                          #players choice on which space
        board[move] = turn
        if( checkWinner(board, 'X') ):                          #checking to see if X wins
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):                       #checking to see if O wins
            print('O wins!')
            break
    
        if turn == 'X':                                         #if no winner the game continues
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
