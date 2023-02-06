import subprocess, os, platform, sys
from colorama import Fore

#Intro information
def intro():
    print(Fore.LIGHTYELLOW_EX + '\nPYTHON LAUNCHER')
    print(Fore.LIGHTMAGENTA_EX + '\n   [' + Fore.LIGHTRED_EX + '!' + Fore.LIGHTMAGENTA_EX + ']' + Fore.LIGHTBLUE_EX + ' This script filter by ' + Fore.LIGHTGREEN_EX + '.py' + Fore.LIGHTBLUE_EX +  ' extension.\n')
    print(Fore.LIGHTBLUE_EX + '   Example: ' + Fore.LIGHTGREEN_EX + '"run script.py"')
    print(Fore.LIGHTBLUE_EX + '   Show dir content: ' + Fore.LIGHTGREEN_EX + '"dir"')
    print(Fore.LIGHTBLUE_EX + '   Move to directory: ' + Fore.LIGHTGREEN_EX + '"cd <directory>"')
intro()

#Clean data
def limpieza():
      if platform.system() == 'Linux':
            subprocess.run("clear", shell=True)
      elif platform.system() == 'Windows':
            subprocess.run("cls", shell=True)


while True:
    #directory path
    pwd1 = subprocess.Popen('cd', stdout=subprocess.PIPE, shell=True)
    (out, err) = pwd1.communicate()
    out1 = str(out[3:-2]).replace("'",'')
    out2 = str(out1[1:]).replace('\\', "/")
    out3 = str(out2).replace('//', '/')
    
    saludo=input(Fore.LIGHTYELLOW_EX + '\n|Console|' + Fore.LIGHTBLUE_EX + ' /' + out3 + Fore.LIGHTMAGENTA_EX + '> ' + Fore.LIGHTGREEN_EX)
    
    #Launcher
    if 'run ' in saludo:
        saludo = '/' + saludo[4:] 
        try:
            print('start wt.exe python C:/' + out3 + saludo)
            subprocess.run("start wt.exe python C:/" + out3 + saludo, shell=True)
        except:
            print(Fore.LIGHTRED_EX + 'This file is not on the actual directory.\n')
    
    #ls
    ls_dir = {'ls', 'dir'} 
    for i in ls_dir:
        if saludo == i:
            limpieza()
            intro()
            print(Fore.LIGHTMAGENTA_EX + '\n|Python scripts|' + Fore.LIGHTGREEN_EX)
            subprocess.run(['dir', '/b', '*.py'], shell=True)
            print(Fore.LIGHTMAGENTA_EX + '\n|Directories|' + Fore.LIGHTGREEN_EX)
            subprocess.run(['dir', '/ad', '/b'], shell=True)
            continue
    
    #cd
    if 'cd ' in saludo:
        try:
            os.chdir(saludo[3:])

        except OSError:
            continue

    #pwd
    if 'pwd' in saludo:
        print('C:/' + out3)
    
    #exit
    if 'exit' in saludo:
        limpieza()
        sys.exit(1)
    
    #Enter
    if saludo == '':
        limpieza()
        intro()
        
        
    
    

