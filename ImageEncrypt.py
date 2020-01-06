# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Library modules you may need 
from Crypto.Cipher import AES 
import hashlib
import sys
import binascii 
import Padding
import os

#######################################
def encrypt(plaintext,key, mode): 
    encobj = AES.new(key,mode) 
    return(encobj.encrypt(plaintext))
    
def ECB_enc(text,key):
    
    ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
    return ciphertext

def CBC_enc(text,key):
    ##https://stackoverflow.com/questions/36834580/iv-must-be-16-bytes-long-error-in-aes-encryption
    iv = os.urandom(16)
    aes_mode = AES.MODE_CBC
    obj = AES.new(key, aes_mode, iv)
    ciphertext = obj.encrypt(text)
    return ciphertext

    
filename = 'tux.ppm'
pic_original = open(filename)
pic_oString = pic_original.read()
pic_original.close()
##saving first 14 characters of file for future deletion
firstLines = (pic_oString[:14])
##deleting the first 3 lines from the original image
pic_oString = pic_oString[14:]

key='secret key'
plaintext = pic_oString
key = hashlib.sha256(key).digest()
# The plain text after padding

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode=0)


ciphertext_ECB =  firstLines +"\n"+ ECB_enc(plaintext,key) 
print(firstLines)

with open("/Users/dianaramirez/Desktop/ECB_tux.ppm", 'wb') as new_ECB:
    new_ECB.write(ciphertext_ECB)



ciphertext_CBC = firstLines +"\n"+CBC_enc(plaintext,key)

with open("/Users/dianaramirez/Desktop/CBC_tux.ppm", 'wb') as new_CBC:
    new_CBC.write(ciphertext_CBC)


