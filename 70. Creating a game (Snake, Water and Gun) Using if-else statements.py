import random
try:
    choices = {0 : "Snake", 1 : "Water", -1 : "Gun"}
    Sn = input("Choose your selection: For Snake press 0, for Water press 1, and for Gun press -1")
    snn = int(Sn)
    cin = random.choice([0, 1, -1])
    print(f"Your selection is : {choices[snn]} , and computer selection is : {choices[cin]}")
    if (snn == cin):
        print("Game is : draw")
    elif (snn == 0) and (cin == 1) or (snn == 1) and (cin == -1) or (snn == -1) and (cin == 0):
        print ("You Win the game")
    else:
        print("Your loss the game")
except KeyError:
    print("You entered an incorrect command, please enter the correct choices")

