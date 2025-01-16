# Prompt the user to enter the filename.
filename = input("Enter file name: ")

# Open the file for reading.
file = open(filename)

# Initialize an empty list to store floating-point numbers.
floatList = []

# Initialize a variable to accumulate the total sum of the floating-point numbers.
total = 0.0

# Iterate over each line in the file.
for line in file:
    # Check if the line starts with the desired prefix.
    if line.startswith("X-DSPAM-Confidence:"):
        # Find the position of the colon in the line.
        colon_position = line.find(":")
        # Extract the number part of the line, strip any extra whitespace.
        number_string = line[colon_position + 1:].strip()
        # Convert the number string to a floating-point number.
        floating_point_number = float(number_string)
        # Append the floating-point number to the list.
        floatList.append(floating_point_number)

# Calculate the total sum of the floating-point numbers in the list.
for number in floatList:
    total += number

# Compute the average of the floating-point numbers.
averageFloat = total / len(floatList)

# Print the calculated average spam confidence.
print("Average spam confidence:", averageFloat)