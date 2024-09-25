import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.cnn.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all 'a' tags and resolve relative links
for link in soup.find_all('a', href=True):
    full_url = urljoin(url, link['href'])
    print(full_url)
