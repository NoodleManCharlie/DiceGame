# Created by Charlie Carter
# 3/27/2025
# Project Title: "Functions & Modules in a Dice Game"
# File Title: "player.py"

# |****IMPORTANT NOTICE****| To run this program, please see "main.py"

# Importing Modules
import string_utils

# Player Variables
playerNames = []


# Defining playerName variable
def defineName(numPlayers):
    for num in range(numPlayers):
        tempPlayerName = input("Player " + str(num + 1) + ", What is your name? \n")
        playerNames.append(string_utils.grammarPolice(tempPlayerName))

    print("Thank you! Onto the game.")
