import requests
import random


url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = response.json()

wordsDB = words["words"]

answerSource = random.choice(wordsDB).upper()