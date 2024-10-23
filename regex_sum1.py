from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def fetch_html(url):
    """Fetch HTML content from a given URL."""
    ctx = ssl.create_default_context()  # Create a default SSL context.
    ctx.check_hostname = False  # Disable hostname checking.
    ctx.verify_mode = ssl.CERT_NONE  # Disable certificate verification.
    with urlopen(url, context=ctx) as response:  # Open the URL.
        return response.read().decode('utf-8')  # Return the decoded HTML content.

def parse_comments(html):
    """Parse HTML and return the sum of numbers in the comments."""
    soup = BeautifulSoup(html, "html.parser")  # Parse the HTML with BeautifulSoup.
    # Sum the numbers in all <span class='comments'> within <tr> tags.
    total = sum(int(span.text) for tag in soup.find_all('tr') for span in tag.find_all('span', class_='comments') if span)  # Only include spans that exist.
    return total  # Return the total sum of comments.

def main():
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'  # URL to fetch.
    html_content = fetch_html(url)  # Fetch the HTML content.
    total_sum = parse_comments(html_content)  # Parse and sum the comments.
    print(f'Sum: {total_sum}.')  # Print the total sum.

if __name__ == "__main__":
    main()  # Execute the main function.