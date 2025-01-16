# Prompt the user to enter the file name and open the specified file.
filename = input("Enter file name: ")
file = open(filename)

# Initialize an empty list to store unique words.
words = []

# Iterate through each line in the file.
for line in file:
    # Split the line into a list of words based on whitespace.
    line_words = line.split()
    # Check each word in the list.
    for word in line_words:
        # If the word is not already in the list, add it.
        if word not in words:
            words.append(word)

# Close the file after reading all lines.
file.close()

# Sort the list of words in alphabetical order.
words.sort()

# Print the sorted list of unique words.
print(words)