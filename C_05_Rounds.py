import random


# generates an integer between 0 and 6
# to simulate a roll of die
def roll_die():
    result = random.randint(1, 6)
    return result


# rolls two dice and returns total whether we
# had a double roll
def two_rolls():
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # checks if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "Yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# Main Routine starts here
print("Press <enter> to begin this round: ")
input()

# Get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# Tell the user if they are eligible for double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points!"

# output initial move results
print(f"You rolled a total of {user_points},  {double_feedback}")

# Get initial dice rolls for computer
computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}.")

# Loop (while both user / computer have <= 13 points)...
# ask user if they want to roll again, update
# points / status

# Roll die for computer and update computer points

# Outside loop - doubler user points if they won and are eligible

# Show rounds result
