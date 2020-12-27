# This is a game of dice

import random

# printTitle takes a string and prints the string in a box of asterisks
def printTitle(text):
    horizontalBorder = "*" * (len(text)+6)
    print(horizontalBorder)
    print("*  " + text + "  *")
    print(horizontalBorder)

# this asks the user to input how many players they want in the game
def setNumPlayer():
    numPlayer = 0
    while numPlayer < 2:
        print("Please enter how many players you want in the game. (Minimum 2)")
        numPlayer = input("Number of players: ")
        if not numPlayer.isdigit():
            print("Error: you must enter a a positive number.")
            numPlayer = 0
        numPlayer = int(numPlayer)
    return numPlayer

# createScoreboard creates a dictionary with n keys, setting all values to 0
def createScoreboard(numPlayer):
    scoreBoard = {}
    for i in range(numPlayer):
        scoreBoard[i] = 0
    return scoreBoard

# rollDie returns a random integer between 1 and 6
def rollDie():
    return random.randint(1,6)

def throwDice(diceAtPlay):
    throwResults = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(diceAtPlay):
        throwResults[rollDie()] += 1
    return throwResults

def countPairs(throwResults):
    pairs = 0
    for count in throwResults:
        if throwResults[count] == 2:
            pairs += 1
    return pairs

def scoreFromThrow(throwResults):
    if throwResults == {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}:
        print("You have a straight! This is worth 1,500 points.")
        diceAtPlay = 0
    elif countPairs(throwResults) == 3:
        print("You have 3 pairs! This is worth 1,500 points.")
        diceAtPlay = 0

def playUntil10k(numPlayer, scoreBoard):
    highestScore = 0
    turnScore = 0
    diceAtPlay = 6
    while highestScore < 10000:
        for player in range(1, numPlayer + 1):
            throwResults = throwDice(diceAtPlay)



def main():
    printTitle("Welcome to Dice 10K!")
    numPlayer = setNumPlayer()
    print("%d players it is! Let's get started." %(numPlayer))
    scoreBoard = createScoreboard(numPlayer)
    winners = playUntil10k(numPlayer, scoreBoard)





main()