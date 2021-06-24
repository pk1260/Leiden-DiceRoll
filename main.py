import random

# Roll dice function
def RollDice():
    roll = random.randint(1, 6)
    rollString = "{}".format(roll)
    text = "Your roll was: "
    print(text)
    print("- - -")
    print("- " + rollString + " -")
    print("- - -" + "\n")
    Menu()

def Menu():
    print("1. Roll a dice")
    print("2. Exit Program" + "\n")

    choice = int(input("enter decision: "))

    if (choice == 1):
        RollDice()
    if (choice == 2):
        exit()

# Execute function
Menu()
