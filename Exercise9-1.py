# Prompt the user to enter the file name.
filename = input('Enter file: ')

# If no file name is entered, default to 'clown.txt'.
if len(filename) < 1:
    filename = 'clown.txt'

# Open the file.
file_handle = open(filename)

# Initialize an empty dictionary to count occurrences of each word.
word_counts = dict()

# Read through the file line by line.
for line in file_handle:
    line = line.strip()  # Remove leading and trailing whitespace.
    words = line.split()  # Split the line into words.

    # Count each word in the line.
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

# Find the most common word and its count.
most_common_word = max(word_counts, key=word_counts.get)
most_common_count = word_counts[most_common_word]

# Print the most common word and its count.
print(most_common_word, most_common_count)