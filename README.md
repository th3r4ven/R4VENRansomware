# R4VEN Ransomware
Simple ransomware, encrypt data via symetric AES-ECB 256 encrypt

It is supposed encrypt to all type of files. 

# How to run:

You can run by typing **python R4VEN_ransomware.py (KEY)**

OBS: **Without (), you can put any key that you want, but need to be length of 32 caracters**

The Crypt key needs to be via argument (You can change that in source code)...


To chosse what directory that will be encrypted, you can modify that via code on main.py:28 or in R4VEN_ransomware.py:23.

Dont forget to put an / at the end.

Eg.: <br>"/home/kali/Documents/" <br>
     "/"<br>
     "/var/www/html/"
