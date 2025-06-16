# Natalie Banks
# June 14 2025
# P1HW2
# This program calculates the remaining budget after accounting for travel expenses.

# Get user input for budget
budget = float(input("Enter your budget: "))
# Get user input for destination
destination = input("Enter your travel destination: ")
# Get user input for gas expenses
gas_expense = float(input("Enter amount you will spend on gas: "))
# Get user input for accommodation expenses
accommodation_expense = float(input("Enter amount you will spend on accommodation: "))
# Get user input for food expense
food_expense = float(input("Enter the amount you will spend on food:"))
# calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense
# calculate remaining budget
remaining_budget = budget - total_expenses
# display results
print("\n--- Travel Budget ---")
print(f"Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaing Budget: ${remaining_budget:.2f}")

