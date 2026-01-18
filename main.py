import os
from getWord import wordsDB, answerSource
from colorama import Fore, Back, init, Style

import subprocess


def screen1():
    os.system('cls' if os.name == 'nt' else 'clear')
    action = ("                         [1] Play            [2] Exit\n\n")

    print("""
                                                                        
                                   ▄▄                  ▄▄                   
                                █▄ ██                  ██                  
                        ▄       ██ ██                  ██       ▄          
        ▀█▄ █▄ ██▀▄███▄ ████▄▄████ ██ ▄█▀█▄      ▄███▀ ██ ▄███▄ ████▄ ▄█▀█▄
         ██▄██▄██ ██ ██ ██   ██ ██ ██ ██▄█▀ ▀▀▀▀ ██    ██ ██ ██ ██ ██ ██▄█▀
          ▀██▀██▀▄▀███▀▄█▀  ▄█▀███▄██▄▀█▄▄▄     ▄▀███▄▄██▄▀███▀▄██ ▀█▄▀█▄▄▄
                                                                    
                                                                    """)

    print(action)
    selection = int(input("=== Selection: "))

    if selection == 1:
        screen2()
    elif selection == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    
def screen2():
    os.system('cls' if os.name == 'nt' else 'clear')
    action = ("                      [1] Classic Wordle            [2] Custom\n\n")

    print("""
                                                                        
                                   ▄▄                  ▄▄                   
                                █▄ ██                  ██                  
                        ▄       ██ ██                  ██       ▄          
        ▀█▄ █▄ ██▀▄███▄ ████▄▄████ ██ ▄█▀█▄      ▄███▀ ██ ▄███▄ ████▄ ▄█▀█▄
         ██▄██▄██ ██ ██ ██   ██ ██ ██ ██▄█▀ ▀▀▀▀ ██    ██ ██ ██ ██ ██ ██▄█▀
          ▀██▀██▀▄▀███▀▄█▀  ▄█▀███▄██▄▀█▄▄▄     ▄▀███▄▄██▄▀███▀▄██ ▀█▄▀█▄▄▄
                                                                    
                                                                    """)

    print(action)
    selection = int(input("=== Selection: "))

    if selection == 1:
        subprocess.run(["python3", "wordleClone.py"])
    elif selection == 2: 
        subprocess.run(["python3", "customWordleClone.py"])
    
screen1()