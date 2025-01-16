filename = input("Enter file name: ")  # Prompt the user to enter the file name.
count = 0  # Initialize a counter to keep track of lines that start with 'From '.

# Open the specified file in read mode.
with open(filename, 'r') as file:
    for line in file:  # Iterate over each line in the file.
        line = line.strip()  # Remove any leading or trailing whitespace from the line.
        if line.startswith('From '):  # Check if the line starts with 'From '.
            words = line.split()  # Split the line into words.
            print(words[1])  # Print the second word, which is the email address.
            count += 1  # Increment the counter.

# Print the total number of lines that started with 'From '.
print(f"There were {count} lines in the file with From as the first word")