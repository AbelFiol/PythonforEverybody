import urllib.request, urllib.parse, urllib.error

file = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')  # Open the URL and retrieve the file.

for line in file:
    print(line.decode().strip())  # Decode bytes to string, strip whitespace, and print.