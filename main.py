__author__ = "Toktatop"
try:
    import os
except:
    pass
# def
def cls():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")



try:
    with open(r"config\isopened.txt", "r") as f:
        isopen = True
except:
    isopen = False
    with open(r"config\isopened.txt", "w") as f:
        f.write('True')

try:
    with open(r"config\color.txt", "r") as f:
        selectbt = f.read()
        isopen = True
except:
    isopen = False

try:
    with open(r"config\name.txt", "r") as f:
        a = f.read()
    if a == "save mode":
        with open(r"config\name.txt", "w") as f:
            f.write("test")
        os.system(r"python funct\savefunct\savemode.py")

except:
    isopen = False
try:
    with open(r"config\lang.txt", "r") as f:
        language = f.read()
    if language == '123456789':
        print("why language is 123456789? now it gonna be '1'")
        language = '1'
        input("press enter to continue>> ")
        cls()
except:
    isopen = False



try:
    from colorama import *
    import string
    import os
    import time
    import subprocess
    from subprocess import call
    import platform
    import requests
    import zipfile
except:
    os.system("pip install requests")
    os.system("pip install platform")
    os.system("pip install subprocess")
    os.system("pip install string")
    os.system("pip install colorama")
    print("critical error 009 can't find modules we can't continue.")
    os.system(r"python funct\reload.py")
try:
    from playsound import playsound
except:
    os.system("pip install playsound")
    cls()



# zapusk bibloetek
init()

# zapusk peremenih
testopen = 0
version_url = 'https://raw.githubusercontent.com/Toktatop/system-ATRIN/main/versionsys.txt'
update_url = 'https://github.com/Toktatop/system-ATRIN/archive/refs/heads/main.zip'
updateneed = 0
current_version = 'systemATRIN0.5'
zip_path = "systemATRIN.zip"
extract_path = ""


# language
if isopen == False:

    while True:
        print('select language')
        print('1 = english')
        print('2 = russian')
        try:
            language = input(">> ")
            cls()
            if language == "1":
                with open(r"config\lang.txt", "w") as f:
                    f.write(language)
                break
            elif language == "2":
                with open(r"config\lang.txt", "w") as f:
                    f.write(language)
                break
            else:
                continue
        except:
            if isopen == False:
                print("error 007 not found language")
                input()
                cls()
                language = '1'
            else:
                pass
if language == '1':
    language = '1'
elif language == '2':
    language = '2'
if isopen == False:
    while True:
        print(Back.YELLOW + Fore.BLACK + "What color for the background and text do you want?" + Fore.RESET + Back.RESET)
        print(Fore.LIGHTWHITE_EX + Back.BLACK + "1 = White text and black background" + Fore.RESET + Back.RESET)
        print(Fore.BLACK + Back.LIGHTWHITE_EX + "2 = Black text and white background" + Fore.RESET + Back.RESET)
        print(Back.YELLOW + Fore.BLACK + "3 = black text and yellow background" + Fore.RESET + Back.RESET)
        print("4 = standard text")
        print(Fore.LIGHTGREEN_EX + Back.BLACK + "5 = green text and black background" + Fore.RESET + Back.RESET)
        selectbt = input(">> ")
        if selectbt == '1':
            with open("config\color.txt", 'w') as f:
                f.write(selectbt)
            break

        elif selectbt == '2':
            with open("config\color.txt", 'w') as f:
                f.write(selectbt)
            break

        elif selectbt == '3':
            with open("config\color.txt", 'w') as f:
                f.write(selectbt)
            break

        elif selectbt == '4':
            with open("config\color.txt", 'w') as f:
                f.write(selectbt)
            break

        elif selectbt == '5':
            with open("config\color.txt", 'w') as f:
                f.write(selectbt)
            break

        else:
            cls()
            continue

if selectbt == '1':
    print(Fore.LIGHTWHITE_EX + Back.BLACK + "Press Enter to continue")
    input(">> ")
    cls()

if selectbt == '2':
    print(Fore.BLACK + Back.LIGHTWHITE_EX + "Press Enter to continue")
    input(">> ")
    cls()

if selectbt == '3':
    print(Back.YELLOW + Fore.BLACK + "Press Enter to continue")
    input(">> ")
    cls()

if selectbt == '4':
    print("Press Enter to continue")
    input(">> ")
    cls()

if selectbt == '5':
    print(Fore.LIGHTGREEN_EX + Back.BLACK + "Press Enter to continue")
    input(">> ")
    cls()

else:
    pass

try:
    if language == '1':
        # warning

        c = 'after writing text please press button Enter!!!'

        # panel
        systemversion = "0.5"

        hello = "write pls your name>> "

        helloadmin = "hello: administrator"

        helloa = "hello"

        entercontinue = "for continue please click Enter>> "

        # system panel 1

        systeminstalled1 = "/downloaded program1/:"

        opencalcinsystem = "open calculator = 'k'"

        opennotepadsystem = "open notepad = 'b'"

        openpasschecksystem = "open password strength checker = 'o'"

        opencreditssystem = "credits = 'c'"

        managerapppage1 = "page 1 is open to open the second click '2'"

        # system panel 2

        systeminstalled2 = "/downloaded program2/:"

        openkalcodesystem = "open kalcode only russian language = 't'"

        opensystemversion = "info system version = 'ver'"

        openexplorer = "open explorer = 'expl'"

        openmsedge = "open Microsoft Edge = 'edge'"

        managerapppage2 = "page2 is open to open the 3 click '3'"

        # system panel 3

        systeminstalled3 = "/downloaded program3/"

        opendos = "open dos (terminal) = 'dos'"

        openpip = "open pip help (pip is manager plugins) = 'pip help'"

        opensetting = "open setting = 'set'"

        openupd = "open update manager = 'upd'"

        managerapppage3 = "page3"

        # calculator

        systemopenedcalc = "/the system successfully opened the calculator/"

        writeoperationonthecalc = "enter operation'+, -, *, /'>> "

        writefirstnumbercalc = "enter the first number>>"

        writeothernumbercalc = "enter the second number>> "

        resultcalc = "result"

        # notepad

        systemopenednotepad = "/system successfully opened notepad/"

        ifyouhavesavednotepad1 = "if there is already a saved text and you want to see it, then click on '1'"

        ifyouhavesavednotepad2 = "if you want to open the second saved text then click on '2'"

        butifyouwantcreatnotepad1 = "and if you want to create a text then press 's1'"

        butifyouwantcreatnotepad2 = "and if you want to create a second text press 's2'"

        creatingtextinnotepad = "write the text you want to save>> "

        yourtextsavednotepad = "your text is saved"

        j1 = "you haven't created the text yet!!"

        j2 = "you haven't created the text yet!!"

        v = 'after saving the text, it will not be possible to add text to it, it will only be possible to change the ' \
            'entire ' \
            'text!!!!!'

        # test code
        systemopenedtestcode = "/system successfully opened password strength checker/"

        writecode = "write code>> "

        resultcode = "Password Strength: %s from 5"

        # version app
        systemversionis = "system version"

        rulersystemversionis = "ruler version 1.0"

        thefirstversionis = "the first created ATRIN system"

        ifyouwantexitver = "if you want exit press button ENTER"

        antivalueerrorcalc = "no letters allowed!!"

        antidelitnanoljcalc = "can't divide by zero"

        antioperationerrorcalc = "wrong operation selected"

        # credits
        creditscreated = "created by company: ATRIN"

        creditdesignandprogramming = "design by Topkatop programmed by Topkatop"

        creditcreatein = "created in python"

        creditrpeoplewhocreate = "people who created the system: Topkatop"

        credithankforreading = "thanks for reading all of this"

        # kolcode

        per1 = "you dont have redacted per1"

        per2 = "you dont have redacted per2"

        per3 = "you dont have redacted per3"

        per4 = "you dont have redacted per4"

        # explorer

        notfoundexpl = "we dont founded explorer in your system"

        # edge

        notfoundedge = "we dont founded microsoft edge in your system"

        # pip package
        pipversion = "(version pip is 0.1)"

        pipendpllugin = "end plugin>> "

        pipnotfounded = "not founded"

        # other

        exittext = "if you wanna exit write 'exit'"
except:
    print("error 007 not found language")
    input()
    cls()
    language = '1'

# privetsvija
cls()
if isopen == False:
    print(c)

    a = input(hello)

    print()
    with open(fr"config\name.txt", "w") as nf:
        nf.write(a)

    cls()


# dlja razrabotchika

if a == 'test':

    print(helloadmin)

else:

    print(helloa, a)

print()

if a == 'test':

    print("version", a)

else:

    print("version", systemversion)

print()

print(c)

print()

# prodolzhit

a1 = input(entercontinue)

print()

cls()


a2 = True

while a2:

    # vse eto glavnij ekran

    # a eto dlja razrabochika

    if a == 'test':

        print("version", a)

    else:

        print("version", systemversion)

    print()

    if a == 'test':

        print(helloadmin)

    else:

        print(f"{helloa}: {a}")

    if a == 'test':

        print()

        print(c)

        print()

        print(systeminstalled1)

        print()

        print(opencalcinsystem)

        print()

        print(opennotepadsystem)

        print()

        print(openpasschecksystem)

        print()

        print(opencreditssystem)

        print(managerapppage1)
        try:
            b = input(">> ")
        except:
            cls()
            continue

        cls()

    else:

        print()

        print(c)

        print()

        print(systeminstalled1)

        print()

        print(opencalcinsystem)

        print()

        print(opennotepadsystem)

        print()

        print(openpasschecksystem)

        print()

        print(opencreditssystem)
        print(managerapppage1)
        try:
            b = input(">> ")
        except:
            continue

        cls()

    if b == '2':
        print()

        print(c)

        print()

        print(systeminstalled2)

        print()

        print(openkalcodesystem)

        print()

        print(opensystemversion)

        print()

        print(openexplorer)

        print()

        print(openmsedge)

        print(managerapppage2)
        try:
            b = input(">> ")
        except:
            continue

        cls()
    if b == '3':
        print()

        print(c)

        print()

        print(systeminstalled3)

        print()

        print(opendos)

        print()

        print(openpip)

        print()

        print(opensetting)

        print()

        print(openupd)

        print(managerapppage3)
        try:
            b = input()
        except:
            continue

        cls()
    if b == 't':
        testopen = 1

    if b == 'k':
        while True:

            # kalkuljator

            print(systemopenedcalc)

            print()

            print(c)

            print()

            k1 = (input(writeoperationonthecalc))

            # kontroller oshibok

            try:

                k2 = float(input(writefirstnumbercalc))

                k3 = float(input(writeothernumbercalc))

            except ValueError:

                print()

                print(antivalueerrorcalc)

                input()

                cls()

                break

            except ZeroDivisionError:

                print()

                print(antidelitnanoljcalc)

                input()

                cls()

                break

            # otvet na zadachi

            if k1 == '+':

                print(resultcalc)

                print(k2 + k3)

                input()

            elif k1 == '-':

                print(resultcalc)

                print(k2 - k3)

                input()

            elif k1 == '*':

                print(resultcalc)

                print(k2 * k3)

                input()

            elif k1 == '/':

                print(resultcalc)

                try:

                    print(k2 / k3)

                except ZeroDivisionError:

                    print()

                    print(antidelitnanoljcalc)

                    input()

                    break

            else:

                print(antioperationerrorcalc)

                input()
                cls()
            print(exittext)
            exitcalc = input(">> ")
            cls()
            if exitcalc == 'exit':
                cls()
                break

    if b == 'b':
        while True:
            # bloknot

            print(systemopenednotepad)

            print()

            print(c)

            print()

            print(ifyouhavesavednotepad1)

            print()

            print(ifyouhavesavednotepad2)

            print()

            print(butifyouwantcreatnotepad1)

            print()

            print(butifyouwantcreatnotepad2)

            print()

            print(exittext)

            print()

            j = input(">> ")

            print()

            cls()

            if j == '1':
                print(j1)

                input()

            if j == '2':
                print(j2)

                input()

            if j == 's1':
                print(v)

                print()

                print(c)

                print()

                j1 = input(creatingtextinnotepad)

                print(yourtextsavednotepad)

                input()

            if j == 's2':
                print(v)

                print()

                print(c)

                print()

                j2 = input(creatingtextinnotepad)

                print(yourtextsavednotepad)

                input()
            if j == 'exit':
                cls()
                break


    if b == 'o':

        # proverka nadezhnosti parolja

        print()

        print(systemopenedtestcode)

        print()

        print(c)

        print()

        password = input(writecode)

        upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])

        lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])

        special = any([1 if i in string.punctuation else 0 for i in password])

        digits = any([1 if i in string.digits else 0 for i in password])

        lenght = len(password)

        if lenght >= 10:

            lenght = True

        else:

            lenght = False

        character = [upper_case, lower_case, special, digits, lenght]

        print(character)

        score = 0

        for i in range(len(character)):

            if character[i]:
                score += 1

        print(resultcode % score)

        print(" ")

        print(" ")

        input()

        cls()

    if b == 'c':
        # crediti

        print(creditscreated)

        print(creditdesignandprogramming)

        print(creditcreatein)

        print(creditrpeoplewhocreate)

        print(credithankforreading)

        input()

        cls()

    if testopen == 1:
        dfg = True

        while dfg:

            if b == 't':

                dfg = True

                testopen = 0

                print("/sistema uspeshno otkrila test/")

                print("nazvanija: kolkode")

                print("ver koda 0.1")

                print("mini kod ")

                print()

                print("eto nenastojashii kod sozdanam nami ")

                print()

                print("esli hotite vijti to nazhmite vvedite 'exit'")

                print()

                print("chtobi otkritj spravku nazhmite 's'")

                print("chtobi nachat programirovatj nazhmite na 'n'")
                kod1 = input(">> ")
                cls()

                if kod1 == 'n':
                    dfg = True

                if kod1 == 's':
                    dfg = True

                if kod1 == 'exit':

                    dfg = False

                    continue

                else:

                    dfg = True

                    pass

                if kod1 == 's':

                    cls()

                    print("""eto ne nastojashii kod 

on sozdan dlja razrabotcikov
kommandi kototrie sushestvujut na etom kode
print=("")
print kommanda nuzhna dlja vivedenija tesksta 
kotorij nado raspechatatj
input=()
vnimanija bez peremenoj nelzja ispolzavatj input=()
nado pisjat tak per1 = input=()
ono predlagaet vvesti tekst polzivatelju vashego koda
stranica 1 chtobi otkritj vtoruju nazhmitje na 2
esli hotite vijti s spravki nazhmite na Enter""")

                    kod2 = input(">> ")

                    cls()

                    if kod2 == '2':

                        cls()

                        print("""=

estj toljko tri peremenih 'per1' 'per2' 'per3'
s pomoshju etogo koda vi mozhete sozdatj peremeniju
peremeniju mozhno ispolzovatj tak :
per1 = input=("vedite vashe imja>> ")
print=(per1)
rezuljtat:
vedite vashe imja>> ja vvedu'test'
test
konec spravki
chtobi vijti s spravki nazhmite na Enter""")

                        input()

                        cls()

                        continue

                if kod1 == 'n':

                    print("sozdavaite kod")

                    print("estj toljko 3 strok")

                    print("esli hotite vo vremja VIPOLNENIJA koda vitje napshite exit")

                    in1 = input()

                    in2 = input()

                    in3 = input()

                    bgh = True

                    while bgh:
                        cls()

                        exittop = input("esli hotite vijte Vvedite 'exit' a esli net to nazhmite na 'Enter'>>")

                        cls()

                        # stroka 1

                        if exittop == 'exit':

                            bgh = False

                            cls()

                            continue

                        elif 'input=(' in in1 or in2 or in3:

                            # in1 input

                            inp1 = in1.replace("input=('", "")

                            inp1 = inp1.replace("')", "")

                            # in2 input

                            inp2 = in2.replace("input=('", "")

                            inp2 = inp2.replace("')", "")

                            # in3 input

                            inp3 = in3.replace("input=('", "")

                            inp3 = inp3.replace("')", "")

                            # per1 check

                            if in1.count("per1 = ") == 1:
                                inp1 = inp1.replace("per1 = ", "")
                                per1 = input(inp1)

                            if in2.count("per1 = ") == 1:
                                inp2 = inp2.replace("per1 = ", "")
                                per1 = input(inp2)

                            if in3.count("per1 = ") == 1:
                                inp3 = inp3.replace("per1 = ", "")
                                per1 = input(inp3)

                            # check per2

                            if in1.count("per2 = ") == 1:
                                inp1 = inp1.replace("per2 = ", "")
                                per2 = input(inp1)

                            if in2.count("per2 = ") == 1:
                                inp2 = inp2.replace("per2 = ", "")
                                per2 = input(inp2)

                            if in3.count("per2 = ") == 1:
                                inp3 = inp3.replace("per2 = ", "")
                                per2 = input(inp3)

                            # check per3

                            if in1.count("per3 = ") == 1:
                                inp1 = inp1.replace("per3 = ", "")
                                per3 = input(inp1)

                            if in2.count("per3 = ") == 1:
                                inp2 = inp2.replace("per3 = ", "")
                                per3 = input(inp2)

                            if in3.count("per3 = ") == 1:
                                inp3 = inp3.replace("per3 = ", "")
                                per3 = input(inp3)

                        if 'print(' in in1 or in2 or in3:
                            # print() 1
                            prin1 = in1.replace("print=('", "")
                            prin1 = in1.replace("')", "")
                            # print() 2
                            prin2 = in2.replace("print=('", "")
                            prin2 = in2.replace("')", "")
                            # print() 3
                            prin3 = in3.replace("print=('", "")
                            prin3 = in3.replace("')", "")
                            if in1.count("per1") == 1:
                                prin1 = prin1.replace("per1", per1)
                                print(prin1)

                            if in2.count("per1") == 1:
                                prin2 = prin2.replace("per1", per1)
                                print(prin2)

                            if in3.count("per1") == 1:
                                prin3 = prin3.replace("per1", per1)
                                print(prin3)

                            # check per2

                            if in1.count("per2") == 1:
                                prin1 = prin1.replace("per2", per2)
                                print(prin1)

                            if in2.count("per2") == 1:
                                prin2 = prin2.replace("per2", per2)
                                print(prin2)


                            if in3.count("per2") == 1:
                                prin3 = prin3.replace("per2", per2)
                                print(prin3)

                            # check per3

                            if in1.count("per3") == 1:
                                prin1 = prin1.replace("per3", per3)
                                print(prin1)

                            if in2.count("per3") == 1:
                                prin2 = prin2.replace("per3", per3)
                                print(prin2)

                            if in3.count("per3") == 1:
                                prin3 = prin3.replace("per3", per3)
                                print(prin3)



                        elif exittop == 'exit':

                            bgh = False

                            print("Nazhmite na Enter chtobi vijte")

                            input(">> ")

                        else:

                            print("ne sushestvuet takoi kommandi oshibka v 1 stroke")

                            input()

    if b == 'ver':
        print(systemversionis, systemversion)
        print(rulersystemversionis)
        print(thefirstversionis)
        print(ifyouwantexitver)
        input(">> ")
        cls()

    if b == 'expl':
        try:
            subprocess.call('C:\Windows\SysWOW64\explorer.exe')
        except:
            print(notfoundexpl)
            input()
            cls()

    if b == 'edge':
        try:
            subprocess.call('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
        except:
            print(notfoundedge)
            input()
            cls()

    if b == 'dos':
        call(["python", "dosterminal\dospy.py"])

    elif "pip" in b:
        b = b.replace("pip", "", 1)
        b = b.replace(" ", "", 1)
        if "help" in b:
            cls()
            b = b.replace("help", "", 1)
            b = b.replace(" ", "", 1)
            if b == '':
                print(r"""____________
            help 'pip'
            for more help of command write 'pip help (command)'
            ____________
            ------------
            command| pip install (plugin from path 'ospip\plugins')
            command| pip help [command or without]
            command| pip uninstall (plugin frm path 'ospip\useplugins')
            command| pip version
            command| pip useplugins
            command| pip plugins
            command| pip run (command from path 'ospip\useplugns')
            ------------
            """)
                input()
                cls()
            elif b == 'install':
                print(r"""____________
install plugin from path 'ospip\plugins'
the basic plugins is (python)
write example 'pip install python'  
____________""")
                input()
                cls()
            elif b == 'run':
                print(r"""____________
run the plugin from path 'ospip\useplugins'
but first you need install plugin from
path 'ospip\plugins'
with command 'pip install example'
____________""")
                input()
                cls()

        elif "version" in b:
            print(pipversion)
            input()
            cls()
        elif "run" in b:
            b = b.replace("run", "", 1)
            b = b.replace(" ", "", 1)
            try:
                eval(b)
                input(pipendpllugin)
                cls()
            except:
                print(pipnotfounded)
                input()
                cls()
                continue
        elif "useplugins" in b:
            os.system(r"dir ospip\useplugins")
            input(">> ")
            cls()
        elif "plugins" in b:
            os.system("dir ospip\plugins")
            input(">> ")
            cls()
        elif "uninstall" in b:
            b = b.replace("uninstall", "", 1)
            b = b.replace(" ", "", 1)
            b = b.replace("python", "pymod", 1)
            try:
                os.system(fr"del ospip\useplugins\{b}.py")
            except:
                print(f"not founded module {b}")
                input("")
                cls()
                continue
            b = b.replace("pymod", "python", 1)
            print(f"module: {b} uninstalled")
            input()
            cls()
        elif "install" in b:
            b = b.replace("install", "", 1)
            b = b.replace(" ", "", 1)
            if b == "python":
                try:
                    om = open(r"ospip\plugins\pymod.le", "r")
                except:
                    print(f"008 error not founded module: {b} 'check version pip or system and look dir plugins'")
                    input(">> ")
                    cls()
                    continue
                svl = om.read()
                om.close()
                com = open(r"ospip\useplugins\pymod.py", "w")
                com.write(svl)
                com.close()
                try:
                    from ospip.useplugins.pymod import *
                except:
                    print(f"when we try ed import module: {b} we had problem")
                    input()
                    cls()
                    continue
                input("we imported python>> ")
                cls()
            else:
                try:
                    om = open(fr"ospip\plugins\{b}.le", "r")
                except:
                    print(f"008 error not founded module: {b} 'check version pip or system and look dir plugins'")
                    input(">> ")
                    cls()
                    continue
                line = om.read()
                om.close()
                com = open(fr"ospip\useplugins\{b}.py", "w")
                com.write(line)
                com.close()
                try:
                    globals().update(__import__(f"ospip.useplugins.{b}", fromlist=["*"]).__dict__)
                except:
                    print(f"when we try ed import module: {b} we had problem")
                    input()
                    cls()
                    continue
                input(f"we imported {b}>> ")
                cls()
    elif b == 'set':
        print("""setting
here example command to write
__________________
color
name
__________________""")
        setting = input(">> ")
        cls()
        if setting == 'color':
            while True:
                print(
                    Back.YELLOW + Fore.BLACK + "What color for the background and text do you want?" + Fore.RESET + Back.RESET)
                print(Fore.LIGHTWHITE_EX + Back.BLACK + "1 = White text and black background" + Fore.RESET + Back.RESET)
                print(Fore.BLACK + Back.LIGHTWHITE_EX + "2 = Black text and white background" + Fore.RESET + Back.RESET)
                print(Back.YELLOW + Fore.BLACK + "3 = black text and yellow background" + Fore.RESET + Back.RESET)
                print("4 = standard text")
                print(Fore.LIGHTGREEN_EX + Back.BLACK + "5 = green text and black background" + Fore.RESET + Back.RESET)
                selectbt = input(">> ")
                if selectbt == '1' or '2' or '3' or '4' or '5':
                    with open("config\color.txt", 'w') as f:
                        f.write(selectbt)
                    cls()
                    os.system(r"python funct\reload.py")
                else:
                    cls()
                    continue

        elif setting == 'name':
            print(f"write you'r new name you'r old name = '{a}'")
            newname = input(">> ")
            cls()
            with open(r"config\name.txt", "w") as f:
                f.write(newname)
            os.system(r"python funct\reload.py")
            cls()
    elif b == 'upd':
        print("welcome to the update checker we gonna check for update of that system")
        print("check upadate = 'c'")
        print("download update = 'd'")
        checkupdate = input(">> ")
        cls()


        def check_update(version_url):
            global updateneed
            # Получить текущую версию программы

            # Получить версию программы с удаленного сервера
            response = requests.get(version_url)
            remote_version = response.text.strip()

            # Проверить, нужно ли обновление
            if remote_version != current_version:
                updateneed = 1
                return True
            else:
                updateneed = 0
                return False


        def update_program(update_url):
            # Загрузить обновленную версию программы
            response = requests.get(update_url, stream=True)

            # Сохранить обновленную версию программы на диск
            with open('systemATRIN.zip', 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            os.system(f"del {zip_path}")
            try:
                with open("system-ATRIN-main\main.py", "r") as f:
                    f.read()
                os.system(f"python system-ATRIN-main\main.py")
                exit()
            except:
                os.system("start system-ATRIN-main\main.exe")
                exit()





        if checkupdate == 'c':
            if check_update(version_url) == True:
                print("you have update for update write = 'd' if you don't wanna update press enter")
                checkupdate = input(">> ")
                cls()
            else:
                print("you don't have update!")
                input(">> ")
                cls()
        if checkupdate == 'd':
            if updateneed == 1:
                update_program(update_url)
                cls()
            elif updateneed == 0:
                cls()
                continue






