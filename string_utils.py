# Created by Charlie Carter
# 3/27/2025
# Project Title: "Functions & Modules in a Dice Game"
# File Title: "string_utils.py"

# |****IMPORTANT NOTICE****| To run this program, please see "main.py"

def grammarPolice(name):
    temp = name.lower()
    temp = (temp[0].upper() + temp[1:])
    return temp
