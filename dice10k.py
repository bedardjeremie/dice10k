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
    for i in range(1,numPlayer+1):
        scoreBoard[i] = 0
    return scoreBoard

# rollDie returns a random integer between 1 and 6
def rollDie():
    return random.randint(1,6)

def throwDice(diceAtPlay):
    throwResults = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    diceList = []
    for i in range(diceAtPlay):
        res = rollDie()
        throwResults[res] += 1
        diceList.append(res)
    return throwResults, diceList

def countPairs(throwResults):
    pairs = 0
    for count in throwResults:
        if throwResults[count] == 2:
            pairs += 1
    return pairs

def checkCombos(throwResults):
    combos = [(6,1,4000), (5,1,3000), (6,6,2400), (6,5,2000), (4,1,2000),
              (5,6,1800), (6,4,1600), (5,5,1500), (4,6,1200), (5,4,1200),
              (6,3,1200), (4,5,1000), (3,1,1000), (5,3,900), (4,4,800),
              (6,2,800), (3,6,600), (4,3,600), (5,2,600), (3,5,500),
              (3,4,400), (4,2,400), (3,3,300), (3,2,200)]
    points = 0
    for tup in combos:
        if throwResults[tup[1]] == tup[0]:
            print("You threw %d %ds! This is worth %d points." %(tup[0], tup[1], tup[2]))
            keep = False
            if points > 0:
                keep = input("Do you want to keep your %ds? (yes/no): " %(tup[1])).lower()[0] == "y"
            else:
                print("Added to your score.")
            if points == 0 or keep:
                points += tup[2]
                throwResults[tup[1]] = 0
    return throwResults, points

def checkOnesAndFifties(throwResults, points):
    if throwResults[1] > 0:
        if throwResults[1] == 2:
            print("You threw 2 1s! This is worth 200 points.")
        if throwResults[1] == 1:
            print("You threw a 1! This is worth 100 points.")
        keep = False
        if points > 0:
            keep = input("Do you want to keep them? (yes/no): ").lower()[0] == "y"
        else:
            print("Added to your score.")
        if points == 0 or keep:
            points += throwResults[1]*100
            throwResults[1] = 0
    if throwResults[5] > 0:
        if throwResults[5] == 2:
            print("You threw 2 5s! This is worth 100 points.")
        if throwResults[5] == 1:
            print("You threw a 5! This is worth 50 points.")
        keep = False
        if points > 0:
            keep = input("Do you want to keep them? (yes/no): ").lower()[0] == "y"
        else:
            print("Added to your score.")
        if points == 0 or keep:
            points += throwResults[5]*50
            throwResults[5] = 0
    return throwResults, points

def scoreFromThrow(throwResults):
    if throwResults == {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}:
        print("You have a straight! This is worth 1,500 points.")
        points = 1500
        diceAtPlay = 0
    elif countPairs(throwResults) == 3:
        print("You have 3 pairs! This is worth 1,500 points.")
        points = 1500
        diceAtPlay = 0
    else:
        throwResults, points = checkCombos(throwResults)
        throwResults, points = checkOnesAndFifties(throwResults, points)
        diceAtPlay = 0
        for key in throwResults:
            diceAtPlay += throwResults[key]
    return points, diceAtPlay

def printScoreboard(scoreBoard):
    print("")
    print("Current Scores:")
    for i in range(1, len(scoreBoard) + 1):
        print("Player %d: %d points" % (i, scoreBoard[i]))

def playUntil10k(numPlayer, scoreBoard):
    highestScore = 0
    ongoingScore = 0
    diceAtPlay = 6
    while highestScore < 10000:
        for player in range(1, numPlayer + 1):
            print("")
            print("Player %d, it's your turn!" %(player))
            if diceAtPlay > 0 and ongoingScore > 0:
                print("The last player cumulated %d points and left %d dice for you to play." %(ongoingScore, diceAtPlay))
                if input("Do you want to piggyback? (yes/no): ").lower()[0] == "n":
                    diceAtPlay, ongoingScore = 6, 0
            keepGoing = True
            while keepGoing:
                input("Press enter to roll the dice:")
                throwResults, diceList = throwDice(diceAtPlay)
                print("******************************************")
                print("You threw:", diceList)
                newPoints, diceAtPlay = scoreFromThrow(throwResults)
                if newPoints == 0:
                    print("You get no points on this turn.")
                    ongoingScore = 0
                    diceAtPlay = 6
                    keepGoing = False
                else:
                    ongoingScore = ongoingScore + newPoints
                    print("So far, you have made %d points this round." %(ongoingScore))
                    if diceAtPlay > 0:
                        print("You can roll your remaining %d dice again, or stop and keep your points." %(diceAtPlay))
                        keepGoing = input("Do you want to roll again? (yes/no): ").lower()[0] == "y"
                        if not keepGoing:
                            scoreBoard[player] += ongoingScore
                            highestScore = max(highestScore, scoreBoard[player])
                    else:
                        print("You have used all of your dice, so you must roll again.")
                        diceAtPlay = 6
            printScoreboard(scoreBoard)
    return scoreBoard

def main():
    printTitle("Welcome to Dice 10K!")
    numPlayer = setNumPlayer()
    print("%d players it is! Let's get started." %(numPlayer))
    scoreBoard = createScoreboard(numPlayer)
    scoreBoard = playUntil10k(numPlayer, scoreBoard)
    print("\nThe game is over.")
    printScoreboard(scoreBoard)
    input("\nPress enter to exit.")

main()