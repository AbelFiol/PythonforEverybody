def computepay(hours, rate):
    # Initialize pay to 0.
    pay = 0

    # Check if hours worked exceed 40.
    if hours > 40:
        # Calculate overtime pay.
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        pay = 40 * rate + overtime_pay
    else:
        # Calculate pay for hours worked if 40 or less.
        pay = hours * rate
    
    # Return the calculated pay.
    return pay

# Prompt the user for hours and rate, then compute pay.
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
gross_pay = computepay(hours, rate)

# Print the computed pay.
print("Pay", gross_pay)