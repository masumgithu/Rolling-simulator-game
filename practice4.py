#Dice rolling simulator game

import random

DiceRolling = True
while DiceRolling:
    print(random.randint(1,6))
    PalyAgain = input("Do You Want To roll Again[y/n]:")
    if PalyAgain == "y":
        continue
    else:
        print("Game Over")
        break