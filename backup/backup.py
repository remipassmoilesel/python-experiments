#!/usr/bin/python2.7
# encoding: utf-8

import os
import argparse
import datetime
import subprocess
import sys

# flag de debogage
DEBUG = False;

# liste des dossiers, chemins absolus sans "/" final
foldersToBackup = []
foldersToBackup.append("/home/remipassmoilesel/linux-utils")
foldersToBackup.append("/home/remipassmoilesel/Documents")
foldersToBackup.append("/home/remipassmoilesel/projects")

# racine de la sauvegarde, avec / final
pathWhereBackup = "/mnt/data/backup/"

logName = "log.txt"

# format de date
dateFormat = "%Y-%m-%d-%H-%M-%S"

# liste des dossier pour affichage
foldersStr = "";
for f in foldersToBackup:
    foldersStr += ":" + f

# description succincte du programme affiché dans l'aide
PGRM_DESC = '''
Sauvegarde de dossiers sur le disque dur tradtionnel. Dossiers:  
'''
PGRM_DESC += foldersStr

# prefixe temporaire de nom de dossier lors d'une sauvegarde
tempPrefix = "temp_"

def exitProgram(code=0, msg=""):
    """
    Arret du programme avec affichage éventuel de message
    """
    if msg != "":
        print msg
        
    exit(code)
    
def backup():
    
    # verifier que la racine de sauvegarde existe ou la creer
    if os.path.isdir(pathWhereBackup) == False:
        try:
            print("Le répertoire de sauvegarde n'existe pas: " + pathWhereBackup)
            os.makedirs(pathWhereBackup, 0755)
            print("Le répertoire à été créé avec succés.")
        except:
            exitProgram(1, "Impossible de créer le répertoire: " + pathWhereBackup)
        
    # creer un dossier temporaire de sauvegarde
    now = datetime.datetime.now().strftime(dateFormat)
    tempPath = pathWhereBackup + tempPrefix + now + "/"
    destinationPath = pathWhereBackup + now + "/"
    
    try:
        os.makedirs(tempPath, 0755)
    except:
        exitProgram(1, "Impossible de créer le répertoire: " + tempPath)
        
    # parcourir les dossiers à sauvegarder
    for d in foldersToBackup:
        try:
            # decouper le chemin du dossier a sauvegarder
            pathList = d.split(os.sep)
            last = pathList[len(pathList) - 1]
            zipName = tempPath + last + ".zip"

            # determiner un nom unique
            i = 2
            while os.path.isfile(zipName) or os.path.isdir(zipName):
                zipName = tempPath + last + "_" + str(i) + ".zip"
                i += 1
            
            # compression
            command = "7za a " + zipName + " " + d
            f = open(pathWhereBackup + logName, "a")
            f.write("##\n")
            f.write(command + "\n")
            f.write("##" + "\n")
            subprocess.check_call(command, shell=True, stdout=f, stderr=f)
            
            print("Dossier sauvegardé avec succés: " + d)
            
        except:
            print("Erreur lors de la sauvegarde de: " + d)
            
    # renommer le dossier temporaire
    try:
        subprocess.call("mv " + tempPath + " " + destinationPath, shell=True)
    except:
        print("Erreur lors de la sauvegarde.")
    

if __name__ == "__main__":
    
    # parser les arguments
    parser = argparse.ArgumentParser(description=PGRM_DESC)
   
    # sauvegarde à la semaine
    parser.add_argument("-w", "--week",
                        action="store_true",
                        help="effectuer une sauvegarde hebdomadaire si necessaire")
    
    # sauvegarde à immédiate
    parser.add_argument("-n", "--now",
                        action="store_true",
                        help="effectuer une sauvegarde immédiatement")
    
    # afficher les sauvegardes
    parser.add_argument("-d", "--display",
                        action="store_true",
                        help="afficher les sauvegardes disponibles")
    
    # afficher les sauvegardes
    parser.add_argument("-l", "--log",
                        action="store_true",
                        help="afficher les dernières lignes du journal")
    
    # afficher les sauvegardes
    parser.add_argument("-e", "--edit",
                        action="store_true",
                        help="editer ce script de sauvegarde")
    
    # récupérer les arguments et les mots clefs
    args = parser.parse_args()
    
    # affichage pour debuggage
    if DEBUG:
        print("args: ")
        print(args)
        print
        
    # effectuer la sauvegarde hebdomadaire si necessaire
    if args.week == True:
        
        # verifier si le dossier existe, si non sauvegarde puis arret
        backupNow = True
        if os.path.isdir(pathWhereBackup):
            
            oneWeek = datetime.timedelta(days=7)
            now = datetime.datetime.now()

            for d in os.listdir(pathWhereBackup):
                try:
                    date = datetime.datetime.strptime(d, dateFormat) + oneWeek
                    
                    if date > now:
                        backupNow = False
                        break
                    
                except:
                    if DEBUG:
                        print("Erreur: " + d)
                    continue
        
        if backupNow:
            try:
                backup()
            except:
                exitProgram(1, "Erreur lors de la sauvegarde.")
        else:
            print("Sauvegarde non nécéssaire.")
            
        exitProgram(0, "Fin de la sauvegarde.")
    
    # effectuer une sauvegarde immédiate
    if args.now == True:
        try:
            backup()
        except:
            exitProgram(1, "Erreur lors de la sauvegarde.")
    
        exitProgram(0, "Fin de la sauvegarde.")
     
    # afficher les sauvegardes
    if args.display == True:
        print("Répertoire racine de sauvegarde: " + pathWhereBackup)
        print
        try:
            for i, f in enumerate(os.listdir(pathWhereBackup)):
                print("#" + str(i + 1) + " " + f)
                
                subp = pathWhereBackup + f;
                if os.path.isdir(subp):
                    for f2 in os.listdir(subp):
                        print ("\t - " + f2);
             
        except:
            exitProgram(1, "Impossible de lire le dossier: " + pathWhereBackup)
     
        print
        exitProgram(0)
        
    # afficher le journal
    if args.log == True:
        try:
            subprocess.check_call("tail -n 20 " + pathWhereBackup + logName + " 2> /dev/null", shell=True)
        except:
            exitProgram(1, "Impossible de lire le journal: " + pathWhereBackup + logName)
     
        print
        exitProgram(0)
        
    # editer le script
    if args.edit == True:
        try:
            subprocess.call("vim " + sys.argv[0], shell=True)
        except:
            exitProgram(1, "Impossible d'editer le script: " + sys.argv[0])
     
        print
        exitProgram(0)
        
    # si pas d'arguments aide puis arret    
    print("Vous devez spécifier des arguments.")
    print
    parser.print_help()
    exitProgram(1)
    
