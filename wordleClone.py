from colorama import Fore, Back, init, Style
from getWord import wordsDB, answerSource
import os, subprocess
init(autoreset=True)

# Clear the screen when the program starts
os.system('cls' if os.name == 'nt' else 'clear')

# Print a blank board
initLetter = ""

for i in range (5):
    initLetter += f"{Back.LIGHTBLACK_EX}   {Style.RESET_ALL} "
    

letterAns = [f"{initLetter}"] * 6
for i in letterAns:
    print(f"{i}\n")

# Wordle function    
def wordle(word, answer, currIndex):
    stringExample = answer
    typedWord = word
    answerString = ""
    
    letterDict = {}
    letterIndexDict = {}
    answerDict = [None] * 5
    
    # If input word does not exist in the word database
    if not typedWord.lower() in wordsDB:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Word not found")
        for i in letterAns:
            print(f"{i}\n")
    else:
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
        for i in letterAns:
            print(f"{i}\n")
            
        # If the input word is correct, stop the function
        if typedWord.upper() == stringExample:
            print("Congrats!")
            return

# Main program
count = 0
while count < 6:
    wordToType = input()
    if wordToType.lower() == answerSource.lower():
        wordle(wordToType, answerSource, count)
        break
    while len(wordToType) != 5:
        print(Back.RED + Fore.YELLOW + "Incorrect format, please try again")
        wordToType = input()
    wordle(wordToType, answerSource, count)

    if not wordToType.lower() in wordsDB:
        count = count + 0
    else:
        count = count + 1
    
print(f"The word is {answerSource}")

input("Press any key to continue...")

subprocess.run(["python3", "main.py"])