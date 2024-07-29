# Prompt the user to enter the number of hours worked.
hours = input("Enter Hours: ")

# Prompt the user to enter the hourly rate of pay.
rate = input("Enter Rate: ")

# Convert the input values from strings to floating-point numbers.
f_hours = float(hours)
f_rate = float(rate)

# Initialize the gross pay variable.
gross_pay = 0

# Check if the hours worked exceed 40 (indicating overtime).
if f_hours > 40:
    # Calculate the number of overtime hours.
    overtime_hours = f_hours - 40
    # Calculate the overtime pay (1.5 times the regular rate).
    overtime_pay = overtime_hours * f_rate * 1.5
    # Calculate the total gross pay including overtime.
    gross_pay = 40 * f_rate + overtime_pay
else:
    # Calculate the gross pay without overtime.
    gross_pay = f_hours * f_rate

# Print the total gross pay.
print(gross_pay)