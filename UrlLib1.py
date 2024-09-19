import urllib.request

file = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')  # Open the URL and retrieve the file.

for line in file:
    print(line.decode().strip())  # Decode bytes to string, strip whitespace, and print.