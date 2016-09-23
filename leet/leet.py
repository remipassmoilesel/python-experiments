#!/usr/bin/python2.7
# encoding: utf-8

import sys
import re
import os
import argparse
import subprocess
import shlex
import fileinput

PGRM_DESC = '''
Transformer une banale chaine de caractère en texte badass !
'''

translations = {
    'a' : '@',
    # 'b' : 'b',
    'c' : '<',
    # 'd' : '|)',
    'e' : '3',
    'f' : 'ph',
    'g' : '9',
    # 'h' : '|-|',
    'i' : '1',
    'j' : 'J',
    'k' : '|<',
    'l' : '|',
    # 'm' : '|\/|',
    # 'n' : '|\|',
    'o' : '0',
    # 'p' : 'P',
    # 'q' : 'Q',
    # 'r' : 'R',
    's' : '$',
    # 't' : '7',
    'u' : '|_|',
    'v' : '\\/',
    # 'w' : 'W',
    # 'x' : 'X',
    # 'y' : 'Y',
    # 'z' : 'z'
    }

def exitProgram(code=0, msg=""):
    """
    Arret du programme avec affichage éventuel de message
    """
    if msg != "":
        print msg
        
    exit(code)

if __name__ == "__main__":

    # parser les arguments
    parser = argparse.ArgumentParser(description=PGRM_DESC)
    
    # récupérer les arguments et les mots clefs
    knownArgs, unknown_args = parser.parse_known_args()
    
    # récupérer l'entrée standard seulement si elle n'est pas connectée à un tty, si elle
    # reçoit des données d'un pipe par exemple
    if not sys.stdin.isatty():
        unknown_args.insert(0, sys.stdin.read())
    
    # pas de chaine et pas d'entrée standard, arrêt
    if len(unknown_args) < 1 :
        print("Vous devez spécifier une chaine de caractères.")
        print
        parser.print_help()
        exitProgram(1)
    
    # transformation du texte
    result = "";

    for strg in unknown_args:
        for c in strg:
            if c.lower() in translations:
                result += translations.get(c.lower())
            else:
                result += c
        result += " "
        
    print result
    
