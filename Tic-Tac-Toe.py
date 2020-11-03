# define a print board
# define a player move
# define what is victory
# define what a draw is
# Create a While Loop

# This is not necessary to put here as it exists within the while loop, but it serves to explain the rest of the code
# a little better.
boardValues = {
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' ',
        }

# This will be the turn count.
count = 0

def printBoard():
    # To print out a layout of the board, we can use brackets and dashes to recreate the design of a tic-tac-toe board.
    # We want to use the format() method to be able to enter in values later.
    row1 = '| [{}][{}][{}] |'.format(boardValues[1], boardValues[2], boardValues[3])
    row2 = '| [{}][{}][{}] |'.format(boardValues[4], boardValues[5], boardValues[6])
    row3 = '| [{}][{}][{}] |'.format(boardValues[7], boardValues[8], boardValues[9])

    print('-------------')
    print(row1)
    print('-------------')
    print(row2)
    print('-------------')
    print(row3)
    print('-------------')

def playerMove():
    # Error variable is used to make sure the player does not place an X or O in an already chosen spot.
    error = 0

    # This is basically the same code for player X and player 0, but repeated twice.
    # We use the count (whether even or odd) to determine which player's turn it is.
    # Then we replace the dictionary value with the X or O so that it shows up on the board.
    # A while loop is included so that a player will have to keep trying if they try to choose an invalid spot.
    if count % 2 == 0:
        newValue = int(input('In what numbered spot would you like to place X?: '))
        if boardValues[newValue] == ' ':
            boardValues[newValue] = 'X'
        else:
            while boardValues[newValue] != ' ' and error == 0:
                newValue = int(input('In what numbered spot would you like to place X?: '))
                if boardValues[newValue] == ' ':
                    boardValues[newValue] = 'X'
                    error += 1
                else:
                    continue
    else:
        newValue = int(input('In what numbered spot would you like to place O?: '))
        if boardValues[newValue] == ' ':
            boardValues[newValue] = 'O'
        else:
            while boardValues[newValue] != ' ' and error == 0:
                newValue = int(input('In what numbered spot would you like to place O?: '))
                if boardValues[newValue] == ' ':
                    boardValues[newValue] = 'O'
                    error += 1
                else:
                    continue

def checkVictory():
    # Here each possible victory is defined.
    # If a victory exists, then a 1 will be returned, whereas if it does not exist, a 0 will be returned.
    if boardValues[1] == boardValues[2] == boardValues[3] != ' ':
        return 1
    elif boardValues[4] == boardValues[5] == boardValues[6] != ' ':
        return 1
    elif boardValues[7] == boardValues[8] == boardValues[9] != ' ':
        return 1
    elif boardValues[1] == boardValues[4] == boardValues[7] != ' ':
        return 1
    elif boardValues[2] == boardValues[5] == boardValues[8] != ' ':
        return 1
    elif boardValues[3] == boardValues[6] == boardValues[9] != ' ':
        return 1
    elif boardValues[1] == boardValues[5] == boardValues[9] != ' ':
        return 1
    elif boardValues[3] == boardValues[5] == boardValues[7] != ' ':
        return 1
    else:
        return 0

def checkDraw():
    # Similar to the checkVictory() function, we will return a 1 if a draw exists or a 0 otherwise.
    # Since there are two conditions to be fulfilled, the draw value will always remain 0 until the end
    # of the game, in which it will decide whether or not there is a victory or draw.
    if count == 9 and victory == 0:
        return 1
    else:
        return 0

# This is where the game starts.
while count < 10:
    # For the players' reference, when the game just starts (at count == 0), a board with numbers will be printed.
    # The board will then clear those numbered values from the dictionary.
    if count == 0:
        print('Here are the numbered tiles for reference!')
        boardValues = {
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
        }
        printBoard()
        print()
        print('GAME START')
        print()
        boardValues = {
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' ',
        }

    # Every turn, we will determine if there is either a victory or a draw by using the previously defined functions.
    # The functions will return a 1 if they exist.
    # We also print the board every turn to show the updates after a player moves.
    victory = checkVictory()
    draw = checkDraw()
    printBoard()

    # This is set so that if there exists a victory or a draw, the players have a chance to restart the game.
    # Another while loop is nested to ensure no invalid input is received.
    # If restarting the game, the board values will reset and the while loop will continue at count = 0.
    # If quitting the game, the original while loop will break.
    if draw == 1 or victory == 1:
        if victory == 1 and count % 2 == 0:
            print('Player 2 won!')
        if victory == 1 and count % 2 != 0:
            print('Player 1 won!')
        if draw == 1:
            print("It's a draw!")
        count = input('Would you like to play again? Type 0 to restart and 1 to quit: ')
        while count != '0' and count != '1':
            print('Error. Invalid input! Please try again.')
            count = input('Would you like to play again? Type 0 to restart and 1 to quit: ')
        count = int(count)
        if count == 0:
            boardValues = {
                1: ' ',
                2: ' ',
                3: ' ',
                4: ' ',
                5: ' ',
                6: ' ',
                7: ' ',
                8: ' ',
                9: ' ',
            }
            continue
        else:
            print('GAME OVER')
            break

    # Depending on which player's turn it is, the print statement differs a little.
    # Player 1 is X, and Player 2 is O.
    if count % 2 == 0:
        print("Player 1's Turn!")
        playerMove()

    if count % 2 != 0:
        print("Player 2's Turn!")
        playerMove()

    # After each turn, the turn count will increase by 1.
    count += 1
