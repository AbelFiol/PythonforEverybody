# Define the line of text.
line_of_text = "X-DSPAM-Confidence:    0.8475"

# Find the position of the colon.
colon_position = line_of_text.find(":")

# Extract the substring starting after the colon.
number_string = line_of_text[colon_position + 1:]

# Convert the extracted substring to a floating-point number.
floating_point_number = float(number_string)

# Print the floating-point number.
print(floating_point_number)