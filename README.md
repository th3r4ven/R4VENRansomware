# R4VEN Ransomware
Simple ransomware, encrypt data via symetric AES-ECB 256 encrypt

It is supposed encrypt to all type of files. 

Python Version: 3.8
Libs: pycrypto, sys, so and re

# How to run:

You can run by typing **python R4VEN_ransomware.py (KEY)**

OBS: **Without (), you can put any key that you want, but need to be length of 32 caracters**

The Crypt key needs to be via argument (You can change that in source code)...


To chosse what directory that will be encrypted, you can modify that via code on **R4VEN_ransomware.py:23.**

Dont forget to put an / at the end.

Eg.: <br>"/home/kali/Documents/" <br>
     "/"<br>
     "/var/www/html/"
<br><br><br>

<h2>Decrypting Data</h2>

For decrypting, you can run **python R4VEN_decrypter.py (KEY)**
OBS: **Without (), put the same key that you use to encrypt the data, 32 caracters**

To chosse what directory that will be decrypted, you can modify that via code on **R4VEN_decrypter.py:17.**

Dont forget to put an / at the end.

Eg.: <br>"/home/kali/Documents/" <br>
     "/"<br>
     "/var/www/html/"
<br><br><br>


**Will be updates**
