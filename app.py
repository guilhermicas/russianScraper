import random
import requests
from bs4 import BeautifulSoup
import os.path
from plyer import notification

"""
TODO: Exception handling
Program flow:
        First check if the word file exists (russian.txt):
        if doesnt exist fetch the words from the site and create it.
        If it exists proceed to:
            fetch a random line and notify the word and the translation
"""


def createWordFile():
    print("words.txt doesn't exists, fetching words")
    res = requests.get(
        "https://1000mostcommonwords.com/1000-most-common-russian-words/")

    soup = BeautifulSoup(res.content, 'html.parser')

    with open("words.txt", "w+") as wordFile:
        for idx, td in enumerate(soup.find_all('td')):
            if(idx % 3 == 0):
                wordFile.write(td.get_text() + "\n")
                continue
            wordFile.write(td.get_text() + " ")


if __name__ == "__main__":
    # If the word cache doesnt exist, fetch and create file
    if not os.path.isfile("./words.txt"):
        createWordFile()
    # Fetch random line and create array with Russian word, English Translation and word number
    randomLine = random.choice(open('./words.txt').readlines())

    # Create notification with random line from file
    notification.notify(title='New Word To Learn!',
                        message=randomLine, timeout=30)

    # Enjoy
