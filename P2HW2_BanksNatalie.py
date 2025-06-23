# Natalie Banks
# 6/22/2025
# P2HW2
# Understanding lists in python


# Pseudocode
# 1. Prompt user to enter grade for Module 1.
# 2. Prompt user to enter grade for Module 2.
# 3. Prompt user to enter grade for Module 3.
# 4. Prompt user to enter grade for Module 4.
# 5. Prompt user to enter grade for Module 5.
# 6. Prompt user to enter grade for Module 6.
# 7. Create a list named 'grades_list' containing all six module grades.
# 8. Calculate the lowest grade in 'grades_list'.
# 9. Calculate the highest grade in 'grades_list'.
# 10. Calculate the sum of grades in 'grades_list'.
# 11. Calculate the average of grades in 'grades_list'.
# 12. Display the lowest grade.
# 13. Display the highest grade.
# 14. Display the sum of grades.
# 15. Display the grades average.


# Get grades for each module
module1_grade = float(input("Enter grade for Module 1: "))
module2_grade = float(input("Enter grade for Module 2: "))
module3_grade = float(input("Enter grade for Module 3: "))
module4_grade = float(input("Enter grade for Module 4: "))
module5_grade = float(input("Enter grade for Module 5: "))
module6_grade = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades_list = [module1_grade, module2_grade, module3_grade, module4_grade, module5_grade, module6_grade]

# Calculate statistics
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_grades = sum(grades_list)
average_grades = sum_grades / len(grades_list)

# Display results
print("\n----------Results----------")
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of grades: {sum_grades:.1f}")
print (f"Average: {average_grades:.2f}")
print ("-----------------------------")
