# Prompt the user to enter the number of hours worked and store it in the variable 'hours'.
hours = input("Enter Hours: ")

# Prompt the user to enter the hourly rate and store it in the variable 'rate'.
rate = input("Enter Rate: ")

# Convert the 'hours' input from a string to a float.
hours = float(hours)

# Convert the 'rate' input from a string to a float.
rate = float(rate)

# Calculate the gross pay by multiplying hours by rate.
gross_pay = hours * rate

# Print the gross pay.
print(f"Pay: {gross_pay}")