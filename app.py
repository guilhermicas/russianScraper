
import random
import requests
from bs4 import BeautifulSoup

res = requests.get(
    "https://1000mostcommonwords.com/1000-most-common-russian-words/")

soup = BeautifulSoup(res.content, 'html.parser')

total = []
row = []
for idx, td in enumerate(soup.find_all('td')):
    txt = td.get_text()
    row.append(txt)
    if(idx % 3 == 0):
        total.append(row)
        row = []

res = [random.choice(total), random.choice(total), random.choice(total)]
print(res)
