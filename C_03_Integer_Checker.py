
# Checks that users enter an integer
# that is more than 13

while True:

    error = "Please enter an integer that is more than 13 or more"

    try:
        print()
        my_num = int(input("Enter an integer: "))

        if my_num < 13:
            print(error)
        else:
            print("Your number is ", my_num)

    except ValueError:
        print(error)
