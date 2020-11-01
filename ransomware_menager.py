#  Copyright (c) 2020.
#  This code was designed and created by TH3R4VEN, its use is encouraged for academic and professional purposes.
#  I am not responsible for improper or illegal uses
#  Follow me on GitHub: https://github.com/th3r4ven

from Crypto.Cipher import AES
import base64
from genPassword import get_random_string
import unidecode
import sys


def createCryptKey():
    return get_random_string(16)


def getKey():
    try:
        return sys.argv[1]
    except IndexError:
        key = get_random_string(16)
        print("Senha da criptografia: " + key)
        return key


def crypt(texto_limpo):
    # =================================================================================================================
    # ◥◤  CRYPT STEP BY STEP  ◥◤
    # ▶▶▶▶▶ DATA -> CLEAN_DATA -> SYMMETRIC_DATA -> CRYPTED_DATA -> B64ENCODED_DATA -> 64ENCODED_DATA ◀◀◀◀◀
    # =================================================================================================================

    chave = getKey()
    teste = True
    cont = len(texto_limpo)
    while teste:
        if (cont % 16) == 0:
            teste = False
        else:
            cont += 1
    # SYMMETRIC_DATA
    aes = AES.new(chave, AES.MODE_ECB)
    cryptado = aes.encrypt(texto_limpo.rjust(cont))  # CRYPTED_DATA
    cryptado = base64.b64encode(cryptado)  # B64ENCODED_DATA
    return cryptado.decode()  # 64ENCODED_DATA


def decrypt(texto_crypto, key):
    # =================================================================================================================
    # ◥◤  DECRYPT STEP BY STEP  ◥◤
    # ▶▶▶▶▶ 64ENCODED_DATA -> B64ENCODED_DATA -> CRYPTED_DATA -> BINARY_DATA -> SYMMETRIC_DATA -> DATA ◀◀◀◀◀
    # =================================================================================================================

    aes = AES.new(key, AES.MODE_ECB)
    texto_crypto = texto_crypto.encode()  # B64ENCODED_DATA
    texto_crypto = base64.b64decode(texto_crypto)  # CRYPTED_DATA
    texto_limpo = aes.decrypt(texto_crypto)  # BINARY_DATA
    texto_limpo = texto_limpo.decode('utf-8')  # SYMMETRIC_DATA
    texto_limpo = texto_limpo.lstrip()  # DATA
    return texto_limpo.encode()
