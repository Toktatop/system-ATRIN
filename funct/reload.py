import platform
import os

def cls():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

cls()
os.system("python main.py")


