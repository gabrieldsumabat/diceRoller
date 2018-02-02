import random


def rollDice(inputArray):
    """Simulate rolling dice. Accepts array size of three. Returns a int value representing the total."""
    diceValue = []
    for x in range (0,int(inputArray[0])):
        diceValue.append(random.randint(1, int(inputArray[1])))
    print("Dice rolls: [%s]"%','.join(map(str,diceValue)))
    return sum(diceValue)+int(inputArray[2])
