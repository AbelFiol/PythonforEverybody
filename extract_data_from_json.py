import urllib.request
import json

# URL of the JSON file.
url = 'http://py4e-data.dr-chuck.net/comments_2056826.json'

# Open the URL and load the JSON data.
with urllib.request.urlopen(url) as response:
    json_data = json.loads(response.read().decode())

# Extract and sum up the 'count' values from the 'comments' list.
total_count = sum(int(comment['count']) for comment in json_data['comments'])

# Display the result.
print('Sum:', total_count)