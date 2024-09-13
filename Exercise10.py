# Prompt the user to enter a file name, defaulting to 'clown.txt' if none provided.
filename = input('Enter File: ')
if len(filename) < 1:
    filename = 'clown.txt'

# Use a context manager to open the file.
with open(filename) as file:
    word_count = dict()

    # Process each line in the file.
    for line in file:
        # Split the line into words.
        words = line.split()
        # Count the frequency of each word.
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

# Create a list of tuples with word frequency and word.
sorted_word_counts = sorted((count, word) for word, count in word_count.items())
# Sort the list in descending order.
sorted_word_counts.reverse()

# Print the top 5 most common words and their counts.
for count, word in sorted_word_counts[:5]:
    print(word, count)