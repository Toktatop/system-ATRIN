import os
try:
    from colorama import *
except:
    os.system("pip install colorama")
import random
import time
try:
    import subprocess
    from subprocess import call
except:
    os.system("pip install subprocess")
# launch colorama
init()


# cls


def cls():
    os.system('CLS')


cls()
print("system was crashed and can't start")
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
    elif sys == "runos":
        print(Fore.RED + "system was crashed and can't start" + Fore.RESET)
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
            help (command)
            cls
            open (target)""" + Fore.RESET)
        elif sys == 'dir':
            print('dir give list of files and directory on your path')
        elif sys == 'cd':
            print("with cd you can join the directory")
        elif sys == 'echo':
            print("echo copy your writed text example 'echo hello world' it gonna give = 'hello world'")
        elif sys == 'cls':
            print("the cls clear screen")
        elif sys == 'open':
            print("command 'open' open a file")
    else:
        print(Fore.RED + f"not founded command: {sys}" + Fore.RESET)
