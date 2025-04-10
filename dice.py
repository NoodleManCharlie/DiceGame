# Created by Charlie Carter
# 2/20/2025
# Project Title: "Functions & Modules in a Dice Game"
# File Title: "dice.py"

# |****IMPORTANT NOTICE****| To run this program, please see "main.py"

# Importing Modules
import random

rolls = 0


# Generating Dice Rolls
def rollDice(pname):
    global rolls

    doubleCount = 0

    dice = []
    total = 0
    rolls += 2

    # Rolling first 2 dice
    dice.append(random.randint(1, 6))
    dice.append(random.randint(1, 6))
    total = dice[0] + dice[1]

    print("You rolled a: ")
    for di in dice:
        print(str(di))

    # Checking for doubles in the rolls (Up to 3 times)
    # Checking for double
    if (checkDouble(dice[1], dice[0], doubleCount)):
        dice.append(random.randint(1, 6))
        print("You rolled a: " + str(dice[2]))
        total += dice[2]
        rolls += 1
        doubleCount += 1

        # Checking for Triple
        if (checkDouble(dice[2], dice[1], doubleCount)):
            dice.append(random.randint(1, 6))
            print("You rolled a: " + str(dice[3]))
            total += dice[3]
            rolls += 1
            doubleCount += 1

            # Checking for Quadruple
            if (checkDouble(dice[3], dice[1], doubleCount)):
                dice.append(random.randint(1, 6))
                print("You rolled a: " + str(dice[3]))
                total += dice[3]
                rolls += 1
                doubleCount += 1

    # Resetting DoubleCoSunt
    doubleCount = 0

    # Describing Total Points
    print("Dice roll total for " + pname + " is: " + str(total))

    return total


# Function for Checking Doubles
def checkDouble(dice1, dice2, doubleCount):
    doubleBool = False

    if dice1 == dice2:
        match doubleCount:
            case 0:
                print("DOUBLE! You get an extra roll")
            case 1:
                print("TRIPLE! You get an extra roll")
            case 2:
                print("QUADRUPLE! INCREDIBLE JOB! You get one more roll")
        doubleBool = True

    return doubleBool
