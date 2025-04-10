# Created by Charlie Carter
# 3/27/2025
# Project Title: "Functions & Modules in a Dice Game"
# File Title: "game_logic.py"

# |****IMPORTANT NOTICE****| To run this program, please see "main.py"

# Importing Modules
import player
import dice

# Variable creation
gameRunning = False
numRounds = 5
numRolls = 2
numPlayers = 0


# "Main" Function
def gameLogic():
    global gameRunning

    scores = [0, 0, 0, 0]

    # Running all the name grabbing, round grabbing etc...
    welcome()

    gameRunning = True
    # Game Loop
    while gameRunning == True:
        for round in range(numRounds):
            # Round Total
            total = 0

            print("Rolling dice for Round #" + str(round + 1))

            # Rolling for each player
            for playernumber in range(numPlayers):
                response = input("Player " + str(playernumber + 1) + ", please roll. (y/n): ")
                while response != "y":
                    response = input("Player " + str(playernumber + 1) + ", please roll. (y/n): ")
                # Dealing with score for each player
                scores[playernumber] += dice.rollDice(player.playerNames[playernumber])
                print("That's a total of " + str(scores[playernumber]) + " points for " + player.playerNames[
                    playernumber] + "\n")

            # Give Player chance to look over dice Rolls.
            continueCheck(round)

        # Ending the Game
        results(scores)


# Preliminary assignments and Introduction
def welcome():
    global numRounds, numPlayers

    # Requesting Name of Players
    print("Welcome to Dice Game!")
    while numPlayers < 1 or numPlayers > 4:
        numPlayers = int(input("How many players will be playing? (Max of 4)\n"))
    player.defineName(numPlayers)

    # Requesting number of rounds from the user
    numRounds = int(input("\nHow many total rounds would you like?\n"))
    while numRounds < 1:
        numRounds = int(input("\nHow many total rounds would you like?\n"))


# Give Player chance to look over dice Rolls.
def continueCheck(round):
    # Statement for all rounds other than final
    if (round != (numRounds - 1)):
        continueVar = input("Ready to continue to the next round? (y/n): ")
        while continueVar != "y":
            continueVar = input("Ready to continue to the next round? (y/n): ")
        print(" ")
    # Statement for final round
    else:
        continueVar = input("Ready to see the Winner? (y/n): ")
        while continueVar != "y":
            continueVar = input("Ready to see the Winner? (y/n): ")
        print(" ")


# Ending the game
def results(scores):
    global gameRunning

    # Check highest score
    highestScore = 0
    for score in scores:
        if score > highestScore:
            highestScore = score

    # Find how had the highest score
    winPlayer = scores.index(highestScore)

    # Congratulations & End code
    print("Congratulations " + player.playerNames[winPlayer] + ", you won! You scored a final total of " +
          str(highestScore) + " points!")
    gameRunning = False
