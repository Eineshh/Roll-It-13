import random

# generates an integer between 0 and 6
# to simulate a roll of die
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # checks if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "Yes"

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score



# Checks that users enter an integer
# that is more than 13
def int_check(question):
    while True:

        error = "Please enter an integer that is more than 13 or more"

        try:
            print()
            response = int(input(question))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here

# initialize user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

target_score = int_check("Enter a target score: ")
print(target_score)

while user_score < target_score and comp_score < target_score:

    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"⭐⭐ Round {num_rounds} ⭐⭐")

    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print("Your final score is {us}")
