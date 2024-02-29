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
print()

while user_score < target_score and comp_score < target_score:
    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"⭐⭐ Round {num_rounds} ⭐⭐")

    # Start of as single round

    # initialize 'pass' variables
    user_pass = "no"
    computer_pass = "no"

    # Start Round...
    print("Press <enter> to begin this round: ")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points! ✨")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    # print(f"The computer rolled a total of {computer_points}.")

    # Loop (while both user / computer have <= 13 points)...
    while computer_points <= 13 and user_points <= 13:

        # If user has 13 points, we can assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"

        # ask user if they want to roll again, update
        # points / status
        print()
        if user_pass == "no":
            roll_again = input("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # If user goes over 13 points, tell them that they lose and set points to 0
            if user_points > 13:
                print(f"💥💥💥 Oops! You rolled a {user_points} so your total is {user_points}."
                      f" Which is over 13 points. 💥💥💥")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}.")

        else:
            # If user passes, we don't want to let them roll again!
            user_pass = "yes"

        # if computer has 10 points or more (and is winning), it should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop.
        elif computer_points == "yes":
            pass

        else:

            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # check computer has not gone over...
            if computer_points > 13:
                print(f"💥💥 The computer rolled a {computer_move}, taking their points"
                      f" to {computer_points}. This is over 13 points so the computer loses! 💥💥")
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}. The computer"
                      f" now has {computer_points}.")

        print()
        # Tell user is they are winning, loosing or are in a tie
        if user_points > computer_points:
            result = "🎉🎉🎉 You are ahead! 🎉🎉🎉"
        elif user_points < computer_points:
            result = "😮 The computer is ahead! 😮"
        else:
            result = "It's currently a tie."

        print(f"⟡⟡⟡ Round Update ⟡⟡⟡: {result} ")
        print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

        # if both user and the computer have passed,
        # we need to exit the loop.
        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside loop - double user points if they won and are eligible

    # Show rounds result

    if user_points < computer_points:
        print()
        print("😔 Sorry - You lost this round and no points "
              "were added to your total score. The computer's score has "
              f"increased by {computer_points} points. 😔")

        add_points = computer_points

    # currently does not include double points!
    elif user_points > computer_points:
        # Doubles user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print()
        print(f"😻😻 Yay! You won the round and {user_points} points have "
              f"been added to your score 😻😻")

    else:
        print(f"◇◇ The result for this round is a tie. You and the computer"
              f"both have {user_points} points. ◇◇")

        add_points = user_points

    # end of a single round

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        comp_score += add_points

    # if the user wins, add their points to their score
    elif user_points > computer_points:
        user_score += add_points

    # if it's a tie, add the point to BOTH SCORES
    else:
        comp_score += add_points
        user_score += add_points

    print()
    print(f"🎲🎲 User: {user_score} points | Computer: {comp_score} points 🎲🎲")
    print()

print()
print("Your final score is {us}")
