import requests
from bs4 import BeautifulSoup

url = 'https://example.com' # Replace with the website you want to scrape
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Example: scrape all links on the website
for link in soup.find_all('a'):
    print(link.get('href'))
