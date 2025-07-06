# Natalie Banks
# 7/6/2025
# P4HW2
# editing exiting programs

# Totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Enter employees name
for _ in range(1000):
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    # Stop if sentinel is entered
    match employee_name:
        case "Done":
            break
    # Enter employee's pay rate and hours worked
    pay_rate = float(input("Enter employee's pay rate: "))
    hours_worked = float(input("Enter number of hours worked: "))

    # Calculate overtime hours and hours worked
    overtime_hours = (hours_worked - 40) * (hours_worked > 40)
    regular_hours = hours_worked - overtime_hours

    # Calculate regular pay and overtime pay
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    # Print results
    print("----------------------------------------")
    print("Employee Name:", employee_name)
    print("Hours Worked  Pay Rate  Overtime  Overtime Pay  Regular Pay  Gross Pay")
    print("-------------------------------------------------------------------------")
    print(f"{hours_worked:<14.2f}{pay_rate:<10.2f}{overtime_hours:<10.2f}"
          f"{overtime_pay:<14.2f}{regular_pay:<13.2f}{gross_pay:<10.2f}")
    print()

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

# Final summary
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
