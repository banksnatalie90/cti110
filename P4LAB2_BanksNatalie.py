# Natalie Banks
# July 2 2025
# P4LAB2
# How to write code displaying information to users using loops

repeat_program = "yes"
for _ in range(100):  # fixed loop to allow up to 100 repeats
    if repeat_program.lower() != "yes":
        break

    user_input = input("Enter an integer: ")

    # basic check to see if the input is a number (integer)
    if user_input.lstrip('-').isdigit():
        num = int(user_input)
        if num >= 0:
            # Display multiplication table without using a function
            for i in range(1, 13):
                print(f"{num} * {i:2} = {num * i}")
        else:
            print("The program cannot accept negative values.")
    else:
        print("Invalid input. Please enter an integer.")

    repeat_program = input("\nWould you like to run the program again? ")
