from colorama import Fore, Back, init, Style
init(autoreset=True)
import os
import time

isFinished = 0
def edit():
    
    global isFinished
    while isFinished == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        initLetter = ""
        boardCol = int(input("Column: "))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range (boardCol):
            initLetter += f"{Back.LIGHTBLACK_EX}   {Style.RESET_ALL} "
        print(initLetter)
        boardRow = int(input("Row: "))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        letterAns = [f"{initLetter}"] * boardRow
        for i in letterAns:
            print(i)
            print()
            
        if boardCol < 3 or boardRow < 4:
            print("Board is too small")
            time.sleep(2)
            continue
            
        doesLookGood = input("Looks good? (y/yes/n/no) ")
        if doesLookGood.lower() == "y" or doesLookGood.lower() == "yes":
            isFinished = 1
            os.system('cls' if os.name == 'nt' else 'clear')
            
    return boardCol, boardRow