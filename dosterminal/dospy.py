from colorama import *
import random
import os
import time
import subprocess
from subprocess import call

# launch colorama
init()


# cls


def cls():
    os.system('CLS')


cls()

while True:
    try:
        sys = input(Fore.RESET + "DOS0.1>> " + Fore.RESET)
    except:
        print(Fore.RED + "**unknown error" + Fore.RESET)
    try:
        print(eval(sys))
    except:
        pass
    if sys == 'dir':
        os.system('dir')
    elif 'cd ' in sys:
        sys = sys.replace('cd ', '')
        try:
            os.system(f'cd {sys}')
        except:
            print(Fore.RED + "**not founded cd" + Fore.RESET)
    elif sys == 'runos':
        call(["python", "main.py"])
    elif 'echo ' in sys:
        sys = sys.replace('echo ', '')
        print(sys)
    elif sys == 'cls':
        cls()
    elif sys == '':
        pass
    elif 'open ' in sys:
        sys = sys.replace('open ', '')
        if sys == 'open':
            pass
        else:
            os.system(f"start {sys}")
    elif 'help' in sys:
        sys = sys.replace('help ', '')
        if sys == 'help':
            print(Fore.LIGHTWHITE_EX + """            ---------
            help
            *********
            command help give a list of commands and help can get arguments example 'help dir' it gonna give 
            info about 'dir'
            *********
            ---------
            dir
            cd (target cd)
            echo (text)
            runos [run os systemANTSI0.5]
            help (command)
            cls
            open (target)""" + Fore.RESET)
        elif sys == 'dir':
            print('dir give list of files and directory on your path')
        elif sys == 'cd':
            print("with cd you can join the directory")
        elif sys == 'runos':
            print('runos need for run the systemANTSI0.5')
        elif sys == 'echo':
            print("echo copy your writed text example 'echo hello world' it gonna give = 'hello world'")
        elif sys == 'cls':
            print("the cls clear screen")
        elif sys == 'open':
            print("command 'open' open a file")
    else:
        print(Fore.RED + f"not founded command: {sys}" + Fore.RESET)
