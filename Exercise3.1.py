# Prompt the user to enter the number of hours worked.
hours = input("Enter Hours: ")

# Prompt the user to enter the rate per hour.
rate = input("Enter Rate: ")

# Convert the input values to float.
f_hours = float(hours)
f_rate = float(rate)

# Initialize the variable to store the gross pay.
gross_pay = 0

# Calculate the gross pay based on whether hours worked exceed 40.
if f_hours > 40:
    # Calculate overtime hours and pay.
    overtime_hours = f_hours - 40
    overtime_pay = overtime_hours * f_rate * 1.5
    # Calculate gross pay with overtime.
    gross_pay = 40 * f_rate + overtime_pay
else:
    # Calculate gross pay without overtime.
    gross_pay = f_hours * f_rate

# Print the calculated gross pay.
print(gross_pay)