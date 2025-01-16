# Attempt to convert the user input to a floating-point number.
try:
    score = float(input("Enter Score: "))
# Handle the case where the input is not a valid number.
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
    exit()

# Check if the score is out of the valid range (0.0 to 1.0).
if score < 0.0 or score > 1.0:
    print("Error: The score must be between 0.0 and 1.0.")
    exit()
# Assign a grade based on the score, starting from the highest range.
elif score >= 0.9:
    print("A")
# Check the next range for grade B.
elif score >= 0.8:
    print("B")
# Check the next range for grade C.
elif score >= 0.7:
    print("C")
# Check the next range for grade D.
elif score >= 0.6:
    print("D")
# If none of the above conditions are met, assign grade F.
else:
    print("F")