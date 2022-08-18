from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.nytimes.com')

soup = BeautifulSoup(r.text)

print(soup)