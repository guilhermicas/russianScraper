
import random
import requests
from bs4 import BeautifulSoup

res = requests.get(
    "https://1000mostcommonwords.com/1000-most-common-russian-words/")

soup = BeautifulSoup(res.content, 'html.parser')

count = 0
total = []
row = []
for td in soup.find_all('td'):
    count += 1
    txt = td.get_text()
    row.append(txt)
    #print(txt, end=" ")
    if(count == 3):
        count = 0
        total.append(row)
        row = []
        # print("\n")

print(random.choice(total))
print(random.choice(total))
print(random.choice(total))
