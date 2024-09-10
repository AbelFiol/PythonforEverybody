filename = input("Enter file: ")

# Use a context manager to open the file and ensure it is closed properly.
with open(filename) as file:
    counts = dict()

    for line in file:
        if line.startswith('From '):
            # Extract the hour directly from the time string.
            hour = line.split()[5].split(':')[0]
            counts[hour] = counts.get(hour, 0) + 1

# Sort the hours and print each hour with its count.
for hour in sorted(counts):
    print(hour, counts[hour])