# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        print()
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes / No")


def instruction():
    print('''
    
✦✦✦ Instructions ✦✦✦

First off, you choose a scoring objective (e.g. The first player to score 50 points or more). 

Next, you roll a die to determine how many points you earn for each round. 

The player who comes closest to 13 wins the round. 

If you roll a double on your first roll, you obtain double the amount of points (6 X 2 = 12). If you win the round, 
your score will grow by the number you earned

You receive zero points if you lose the round. 

In a tie, the number of bonus points awarded to each player is the same.  


    ''')


# Main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
