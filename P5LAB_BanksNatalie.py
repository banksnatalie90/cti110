# Natalie Banks
# 7/12/2025
# P5LAB
# Using user defined functions


import random

def disperse_change(change):
   
    # Value to integar
    change = round(change *100)
    print (f"change owed as an integar: ${change}")

    # Value to dollars
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    # Value to quarters
    num_quarters = change // 25
    change = change - (num_quarters * 25)

    # Value of dimes
    num_dimes = change // 10
    change = change - (num_dimes * 10)

    # Value of nickels
    num_nickels = change // 5
    change = change - (num_nickels * 5)

    # Value of pennies
    num_pennies = change

    # Display coins needed
    if num_dollars > 0:
        if num_dollars == 1:
            print (f"{num_dollars } dollar")
        else:
            print (f"{num_dollars } dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print (f"{num_quarters } quarter")
        else:
            print (f"{num_quarters } quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print (f"{num_dimes } dime")
        else:
            print (f"{num_dimes } dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print (f"{num_nickels } nickel")
        else:
            print (f"{num_nickels } nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print (f"{num_pennies } penny")
        else:
            print (f"{num_pennies } pennies")

            



def main():
    # logic


    # Generate the amount owed
    amount_owed = round (random.uniform (0.01, 100.00), 2)
    print (f"You owe:${amount_owed:.2f} ")


    # Create variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout?"))

    # Calculate change owed to customer
    change = money_in - amount_owed
    print (f"change owed: ${change:.2f} ")

    # disperse change
    disperse_change (change)


main()      
