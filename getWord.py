import requests
import random
import json


url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = response.json()

wordsDB = words["words"]

answerSource = random.choice(wordsDB).upper()

def customWordleWord(length):
    requestData = requests.get(f"https://random-words-api.kushcreates.com/api?language=en&length={length}&words=1")

    answerSource = json.loads(requestData.text)[0]["word"]
    category = json.loads(requestData.text)[0]["category"].replace("_", " ").title()
    
    return answerSource, category