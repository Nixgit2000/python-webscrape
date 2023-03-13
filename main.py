import requests
import json
from bs4 import BeautifulSoup

url = "https://www.cbc.ca/news"


response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

stories = soup.find_all('h3')

data = []
for story in stories:
    title = story.text.strip()
    if title not in data:
        data.append(title)

with open('CBC.json', 'w') as f:
    json.dump(data, f)