#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:52:42 2019

@author: dianaramirez
"""
from Crypto.PublicKey import RSA

import tools

def part5A(pkfile,ctfile,possmess):
##convert messages using public key, and compare them

    recovered_public_key = RSA.importKey(open(pkfile, 'r').read())
    public_key = recovered_public_key
    
    
    filepossmess = open(possmess)
    possible_message = filepossmess.readlines()

    
    cyphertxtSent = (open(ctfile)).read()[1:-3]
    
    for ln in possible_message:
        ln = ln[:-1]
        message_int = tools.text_to_int(ln)
        ciphertext = public_key.encrypt(message_int, None)
     
        ciphertext = str(ciphertext[0])
        
        if ciphertext == cyphertxtSent:
            print "Message found: "+ ln 
    
def part5B(ctfile):
    cipher_mess = int((open(ctfile,'r')).read()[1:-3])
    #print(cipher_mess)
    plaintxt = tools.int_to_text(int(tools.find_root(cipher_mess,3)))
    print(plaintxt)

pkfile = '/Users/dianaramirez/Desktop/Computer Security/Assignment1/Supporting_Files/HLand_Key.pub'
ctfile1 = '/Users/dianaramirez/Desktop/Computer Security/Assignment1/Supporting_Files/5A_CipherMessage'
possmess = '/Users/dianaramirez/Desktop/Computer Security/Assignment1/Supporting_Files/5A_messagespace'
part5A(pkfile,ctfile1,possmess)   


unknown_ctfile = '/Users/dianaramirez/Desktop/Computer Security/Assignment1/Supporting_Files/5B_CipherMessage'
part5B(unknown_ctfile)