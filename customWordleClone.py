from colorama import Fore, Back, init, Style
from getWord import customWordleWord
from editBoard import edit
import os, subprocess
init(autoreset=True)

# Clear the screen when the program starts
os.system('cls' if os.name == 'nt' else 'clear')

# Print a blank board
initLetter = ""
col, row = edit()
answerSource, category = customWordleWord(col)

for i in range (col):
    initLetter += f"{Back.LIGHTBLACK_EX}   {Style.RESET_ALL} "
    
print(f"Category: {category}\n")
letterAns = [f"{initLetter}"] * row
for i in letterAns:
    print(i)
    print()

# Wordle function    
def wordleCustom(word, answer, currIndex):
    stringExample = answer
    typedWord = word
    answerString = ""
    
    letterDict = {}
    letterIndexDict = {}
    answerDict = [None] * col

    # Add data of the answer word
    for idx, i in enumerate(stringExample):
        letterDict.update({i.upper(): stringExample.count(i)})
        letterIndexDict.update({idx: i.upper()})

    # If the input letter index is identical to the one of the answer
    for idx, i in enumerate(typedWord):
        if i.upper() == letterIndexDict[idx]:
            answerDict[idx] = ({"char": i.upper(), "color": Back.GREEN + Fore.BLACK})
            letterDict[i.upper()] -= 1
    
    # For other letters that are not at the identical index to the index of the answer, return either yellow or black background        
    for idx, i in enumerate(typedWord):
        if answerDict[idx] is not None:
            continue
        
        if i.upper() in letterDict and letterDict[i.upper()] > 0:
            answerDict[idx] = ({"char": i.upper(), "color": Back.YELLOW + Fore.BLACK})
            letterDict[i.upper()] -= 1
            
        else:
            answerDict[idx] = ({"char": i.upper(), "color": Back.BLACK + Fore.WHITE})
    
    # Combine the answer string    
    for i in range(len(answerDict)):
        answerString = answerString + f"{answerDict[i]['color']} {answerDict[i]['char']} {Style.RESET_ALL} "

    # Replace the current position of the board with the input word, then update it
    letterAns[currIndex] = answerString
    currIndex = currIndex + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Category: {category}\n")
    for i in letterAns:
        print(i)
        print()
    
        
    # If the input word is correct, stop the function
    if typedWord.upper() == stringExample:
        print("Congrats!")
        return

# Main program
count = 0
while count < row:
    wordToType = input()
    if wordToType.lower() == answerSource.lower():
        wordleCustom(wordToType, answerSource, count)
        break
    while len(wordToType) != col:
        print(Back.RED + Fore.YELLOW + "Incorrect format, please try again")
        wordToType = input()
    wordleCustom(wordToType, answerSource, count)

    count = count + 1
    
print(f"The word is {answerSource}")

input("Press any key to continue...")

subprocess.run(["python3", "main.py"])
