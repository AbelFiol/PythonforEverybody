from urllib.request import urlopen
from bs4 import BeautifulSoup

count = int(input('Enter count: '))  # Get the number of times to follow links.
position = int(input('Enter position: '))  # Get the position of the anchor tag.

url = 'http://py4e-data.dr-chuck.net/known_by_Victoria.html'  # Initial URL.

html = urlopen(url).read()  # Read the HTML content.
soup = BeautifulSoup(html, "html.parser")  # Parse the HTML.

tags = soup('a')  # Find all anchor tags.

print(url)  # Print the initial URL.
print(tags[position - 1].get('href'))  # Print the URL of the specified anchor tag.

for i in range(count - 1):  # Loop to follow links the specified number of times.
    tag = tags[position - 1]  # Get the tag at the specified position.

    url = tag.get('href')  # Get the href attribute from the tag.
    html = urlopen(url).read()  # Read the HTML content of the next page.

    soup = BeautifulSoup(html, "html.parser")  # Parse the HTML of the new page.
    tags = soup('a')  # Find all anchor tags on the new page.

    print(tags[position - 1].get('href'))  # Print the URL of the specified anchor tag on the new page.