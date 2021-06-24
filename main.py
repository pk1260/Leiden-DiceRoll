import random

# Roll dice function
def RollDice():
    roll = random.randint(1, 6)
    convert = "Your roll was: {}".format(roll)
    print("\n" + convert + "\n")
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
