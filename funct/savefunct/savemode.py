print("-----------------------------------------")
print("press 'CTRL-C' to exit or write 'exit()'!")
print("-----------------------------------------")
print("write 'help()' to help")
print("-----------------------------------------")
while True:
    savemode = input("save-mode>> ")
    if savemode == "exit()":
        exit(1)
    elif savemode == "help()":
        print("""
----------------
[] = comment
{} = need argument
// = you can write argument if you wan't
----------------
exit() [exit from save-mode]
help() [give help]
echo({text to echo})
conf {the file from config example 'lang' or 'name'} {to what change}""")
    elif 'echo(' in savemode:
        savemode = savemode.replace("echo(", "", 1)
        savemode = savemode.replace(")", "")
        print(savemode)
    elif 'conf ' in savemode:
        savemode = savemode.replace("conf ", "", 1)
        file = savemode[:savemode.find(" ")]
        try:
            with open(f"..\\..\\config\\{file}.txt", 'w') as f:
                savemode = savemode[savemode.find(" ") + 1:]
                savemode = savemode.replace("'_'", " ")
                f.write(savemode)
        except:
            with open(f"config\\{file}.txt", 'w') as f:
                savemode = savemode[savemode.find(" ") + 1:]
                savemode = savemode.replace("'_'", " ")
                f.write(savemode)


