import random
try:
    gamere = [["Draw", "Win", "Loss"], ["Loss", "Draw", "Win"], ["Win", "Loss", "Draw"]]
    game = ["Snake", "Water", "Gun"]
    usinp = int(input("Enter Your choice 0 for snake, 1 for Water and 2 for gun : \n"))
    compinp = random.randint(0, 2)
    fingame = gamere[usinp][compinp]
    print(f"\n Your selection is : {game[usinp]}, and Computer selection is : {game[compinp]}")
    print(f"\n You : {fingame}")
except KeyError:1
print("You entered an incorrect command, please enter the correct choices")

