#!/usr/bin/python2.7
# encoding: utf-8

import sys
import os
import argparse
import subprocess

PGRM_DESC = '''
Memo
'''

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description=PGRM_DESC)
    parser.add_argument("positional", help="argument obligatoire")
    parser.add_argument("-o", "--optional", help="argument optionnel, avec un -")
    parser.add_argument("-o2", "--optional2",
                        help="argument optionnel qui prendra la valeur vraie ou faux",
                        action="store_true")
    
    # parser tous les arguments, erreurs si inconnus
    knownArgs = parser.parse_args()
    
    # parser les arguments connus et inconnus
    knownArgs, unknown = parser.parse_known_args()
    
    print knownArgs.positional
    
    # afficher l'aide
    parser.print_help()
       
