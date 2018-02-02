import inputValid
import rollDice
import re


def diceRoller():
    """Simulates rolling DnD dice."""

    print("""           
             Welcome to the dice roller!
             Format: [#d#(+/-)#]
             Ex. 2d8+4 will roll two eight sided dice and add four.   
            """)
    while (1):
        diceInput = input("Enter dice to be rolled:")
        while not inputValid.inputValid(diceInput):
            diceInput = input("Invalid input, please try again.\n")
        inputValues = re.split('[\D]', diceInput)
        diceResult = rollDice.rollDice(inputValues)
        print("The dice result is : " + str(diceResult))


if __name__ == "__main__":
    diceRoller()
