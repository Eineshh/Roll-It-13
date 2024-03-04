# finds the lowest, highest and average score from a list
def get_stats(stats_list):
    pass

    # sort the lists.
    stats_list.sort()

    # find the lowest, highest and average scores...
    user_low = stats_list[0]
    user_high = stats_list[-1]
    user_average = sum(stats_list) / len(stats_list)


# create lists to hold user and computer scores
stats_list = [10, 0, 13, 7, 10, 11]
comp_scores = [10, 11, 0, 0, 10, 11]

# Loop six times - for testing purposes, ask the user to enter the
# score for the user and the computer for each round
# for item in range(0, 6):
#     user_score = int(input("Enter the user score: "))
#     comp_score = int(input("Enter the computer score: "))
#
#     # add user score to list of user scores!
#     user_scores.append(user_score)
#     comp_scores.append(comp_score)

# calculate the lowest, highest and average
# scores and display them.

print()
print("Low: ", user_low)
print("High: ", user_high)
print("Average: ", user_average)
