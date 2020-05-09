import os, random

def cls(): #Standard clear termincal function for Unix / Windows
    os.system('cls' if os.name=='nt' else 'clear')

def printBoard(board): #Prints the board (dictionary) passed to it
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('---+---+---')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('---+---+---')
    print(board[1] + '|' + board[2] + '|' + board[3])

def userMove():
    while True:
        try:
            choice = int(input())
            if theBoard[choice] == '   ': #Checks to see if users choice is free
                theBoard[choice] = ' X '
                break
            elif theBoard[choice] == ' X ' or ' O ': #If the space is not free, print error message and try again
                print("That space is already taken! Please choose another")
            else:
                printBoard(theBoard) #If the user chooses and int other than 1 - 9, print error message and try again
                print("Only choose a number between 1 and 9")
        except:
            printBoard(theBoard) #If a user puts a non-int print error message and try again
            print("Error, please try again!")

def computerMove():
    while True:
        computerChoice = random.randint(1, 9)
        if theBoard[computerChoice] == '   ':
            theBoard[computerChoice] = ' O '
            break

def checkWin(i):
    if theBoard[7] == i and theBoard[8] == i and theBoard[9] == i:
        return True
    elif theBoard[4] == i and theBoard[5] == i and theBoard[6] == i:
        return True
    elif theBoard[1] == i and theBoard[2] == i and theBoard[3] == i:
        return True
    elif theBoard[7] == i and theBoard[4] == i and theBoard[1] == i:
        return True
    elif theBoard[8] == i and theBoard[5] == i and theBoard[2] == i:
        return True
    elif theBoard[9] == i and theBoard[6] == i and theBoard[3] == i:
        return True
    elif theBoard[7] == i and theBoard[5] == i and theBoard[3] == i:
        return True
    elif theBoard[1] == i and theBoard[5] == i and theBoard[9] == i:
        return True
    else:
        return False

theBoard = {7: '   ', 8: '   ', 9: '   ',
            4: '   ', 5: '   ', 6: '   ',
            1: '   ', 2: '   ', 3: '   '}

cls()
print("Welcome to Naughts and Crosses 3000!")
printBoard(theBoard)
print("The board matches your number pad, you are X's, where would you like to go?")

while True:
    userMove() #User chooses a square, and draws an 'X'
    if checkWin(" X ") == True: #Checks if user wins
        cls()
        printBoard(theBoard)
        print("--- You win! ---")
        break

    if '   ' in theBoard.values(): #Checks for empty squares
        computerMove() #Computer chooses a random empty square, and draws a 'O'
        cls()
        if checkWin(" O ") == True: #Checks if computer wins
            cls()
            printBoard(theBoard)
            print("--- You lose! ---")
            break
    else:
        cls()
        printBoard(theBoard)
        print("--- Draw! ---")
        break
    printBoard(theBoard) #Prints the updated board with user and computer moves