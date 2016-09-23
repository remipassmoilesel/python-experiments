'''
Created on 10 janv. 2016

@author: remipassmoilesel
'''

import os
import sys
import shutil
import subprocess

# itérer les lignes d'un fichier
for line in open("file.txt", 'r'):
    print line

# ecrire dans un fichier
command = "ls"
logName = "test.log"
with open(logName, "a+") as outfile:
    # flusher après chaque sortie ou le fichier de journal paraitra en désordre
    outfile.write("\n#c#: " + command + "\n")
    outfile.flush()
    subprocess.call(command, stdout=outfile, stderr=outfile, shell=True)
    outfile.flush()

# tester les droits d'-un fichier
def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

# chemin du script
print "sys.argv[0]"
print sys.argv[0]

# chemin absolu
print "os.path.abspath(__FILE__)"
print os.path.abspath(__file__)

# resolution de chemin
print os.path.realpath(__file__)

# extraire le chemin du dossier
print "os.path.dirname(__file__)"
dirname = os.path.dirname(os.path.abspath(__file__))

print dirname

# assembler des chemin
print os.path.join(dirname, "log.txt")

# lister les lignes d'un fichier
with open("fname.txt") as f:
    content = f.readlines()

# verifier si un dossier existe
if os.path.isdir("/home/el") == False:
    print("Dossier invalide")
   
# lister un répertoire
path = "/dir/to/list" 
dirList = os.listdir(path)
for fname in dirList:
    print fname

# créer des dossiers
os.makedirs("newpath")

# lister les parties d'un chemin
your_path = r"d:\stuff\morestuff\furtherdown\THEFILE.txt"
path_list = your_path.split(os.sep)
print path_list

# créer un fichier vide, "touch"
open("path/to/file", 'a').close()

# copier un fichier
shutil.copy("path/source", "path/Dest")







