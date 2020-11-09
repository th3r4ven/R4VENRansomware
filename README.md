# R4VEN Ransomware
Simple ransomware, encrypt data via symetric AES-ECB 256 encrypt

It is supposed encrypt to all type of files. 

# How to run:

## Step a Step

1. Alter the folder target in file `R4VEN_ransomware.py` in variable `path`
1. pip install -r requirements.txt
1. python call.py > hash.key
1. cat hash.key | python R4VEN_ransomware.py

All Done :)

You can run by typing **python R4VEN_ransomware.py (KEY)**

OBS: **Without (), you can put any key that you want, but need to be length of 32 caracters**

The Crypt key needs to be via argument (You can change that in source code)...


To chosse what directory that will be encrypted, you can modify that via code on main.py:28 or in R4VEN_ransomware.py:23.

Dont forget to put an / at the end.

Eg.: <br>"/home/kali/Documents/" <br>
     "/"<br>
     "/var/www/html/"
<br><br><br>
**Will be updates**


## Docker

A Dockerfile created a image base to you in outher projects, this image is for example this project in your machine in safeted. And encrypt all data in folder `/home/`

     docker build -t ther4ven/r4venransomware .

     docker run ther4ven/r4venransomware