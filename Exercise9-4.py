# Prompt the user for the filename.
filename = input("Enter file: ")
# Open the file.
file = open(filename)

# Initialize an empty dictionary to store email counts.
counts = dict()

# Read through the file line by line.
for line in file:
    if line.startswith('From '):
        # Split the line into words.
        words = line.split()
        # The email address is the second word.
        email = words[1]
        # Update the dictionary with the count for this email.
        counts[email] = counts.get(email, 0) + 1

# Find the email with the highest count.
# Use the max function with the key argument to get the email with the highest count.
max_email = max(counts, key=counts.get)
max_count = counts[max_email]

# Print the result.
print(max_email, max_count)