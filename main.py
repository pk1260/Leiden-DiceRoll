import random

# Roll dice function
def RollDice():
    roll = random.randint(1, 6)
    convert = "Your roll was: {}".format(roll)
    print(convert)

# Execute function
RollDice()
