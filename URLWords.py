import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')  # Open the URL and retrieve the file.

counts = dict()  # Initialize an empty dictionary to store word counts.

for line in file:
    words = line.decode().split()  # Decode bytes to string, then split the line into words.

    for word in words:
        counts[word] = counts.get(word, 0) + 1  # Update word count in the dictionary.

print(counts)  # Print the dictionary containing word counts.