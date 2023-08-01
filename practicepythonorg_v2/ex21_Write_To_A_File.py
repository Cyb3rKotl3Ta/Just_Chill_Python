from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.nytimes.com')

soup = BeautifulSoup(r.text)  

prettified_html = soup.prettify()

file_path = 'practicepythonorg_v2/files_for_ex/ex21.html'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(prettified_html)

print(f"Successfully written the BeautifulSoup content to '{file_path}'.")
