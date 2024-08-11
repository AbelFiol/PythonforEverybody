# Open the file 'mbox-short.txt' for reading.
filename = open('mbox-short.txt')

# Iterate over each line in the file.
for line in filename:
    # Remove any leading and trailing whitespace from the line.
    line = line.strip()
    # Convert the line to uppercase and print it.
    print(line.upper())