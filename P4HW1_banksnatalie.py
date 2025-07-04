# Natalie Banks
# July 4 2025
# P4HW1
# Score Processing with Validation and Loop


# Ask user how many scores to enter
num_scores = int(input("How many scores would you like to enter? "))

# List to store valid test scores
test_scores = []

# Collect scores using a loop
for i in range(num_scores):
    print(f"Enter score #{i + 1}: ", end="")
    score = float(input())

    # Validate score (must be 0-100)
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        print(f"Enter score #{i + 1} again: ", end="")
        score = float(input())

    test_scores.append(score)  # Add valid score to the list

# Drop the lowest score
lowest_score = min(test_scores)
test_scores.remove(lowest_score)

# Calculate average
average_score = sum(test_scores) / len(test_scores)

# Determine letter grade
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("\n---------- Results ----------")
print(f"Lowest score       : {lowest_score:.2f}")
print(f"Modified score list: {test_scores}")
print(f"Average score      : {average_score:.2f}")
print(f"Letter grade       : {letter_grade}")

