#!/usr/bin/python2.7
# encoding: utf-8
'''

'''

import os
import subprocess

def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

if __name__ == "__main__":
    
    # Récupérer le path
    path = os.environ['PATH']
    
    rslt = "Path: " + path + "\n";
    
    # decouper le path
    for p in path.split(":"):
        
        rslt += "\n## " + p
        
        # lister les dossier
        for f in os.listdir(p):
            fa = os.path.join(p, f)
            if(is_exe(fa)):
                rslt += f + "\n"
        
    print rslt




