# Prompt the user to enter a score.
score = input("Enter Score: ")

# Convert the input from a string to a floating-point number.
score = float(score)

# Check if the score is out of the valid range (0.0 to 1.0).
if score < 0.0 or score > 1.0:
    print("Error: The score must be between 0.0 and 1.0.")
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