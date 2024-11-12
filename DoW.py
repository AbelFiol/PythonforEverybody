# Open the file named 'mbox-short.txt'.
email_file = open('mbox-short.txt')

# Iterate through each line in the file.
for line in email_file:
    # Remove any trailing whitespace from the line.
    stripped_line = line.rstrip()
    
    # Split the line into words based on whitespace.
    words_list = stripped_line.split()

    # Check if the line has fewer than 3 words or does not start with 'From'.
    if len(words_list) < 3 or words_list[0] != 'From':
        continue  # Skip to the next line if the condition is met.
    
    # Print the third word in the line (the day of the week).
    print(words_list[2])