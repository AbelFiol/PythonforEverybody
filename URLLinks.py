import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt the user for a URL.
url = input('Enter - ')

# Retrieve the web page.
html = urllib.request.urlopen(url, context=ctx).read()

# Parse the HTML using BeautifulSoup.
soup = BeautifulSoup(html, 'html.parser')

# Find all anchor tags ('a') in the HTML.
tags = soup('a')

# Print the value of the 'href' attribute for each anchor tag.
for tag in tags:
    print(tag.get('href', None))