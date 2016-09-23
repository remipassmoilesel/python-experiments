#!/usr/bin/python2.7
# encoding: utf-8

# Commandes 

import os
import subprocess
import shlex
import datetime
import json
import traceback
import argparse


# conserver l'heure de l'appel
date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")

# emplacement du script
scriptDir = os.path.dirname(os.path.abspath(__file__));
scriptDir = os.path.join(scriptDir, "installation/");

# racine des journaux
logRoot = os.path.join(scriptDir, "log/")

# nom du journal a utiliser
logName = os.path.join(logRoot, "installation_" + date + ".txt");

# le fichier de données, chemin absolu uniquement
installationFilePath = os.path.join(scriptDir, "installation.json"); 

# installationFilePath = "./installation.json"

# les identifiants de sections
beforeCommandsId = "before_commands"
afterCommandsId = "after_commands"
toInstallId = "to_install"
toUninstallId = "to_uninstall"

readableNames = {
                 beforeCommandsId : "Commandes préliminaires",
                 toInstallId : "Paquets à installer",
                 toUninstallId : "Paquets à désinstaller",
                 afterCommandsId : "Commandes finales",
}

# descirption du programme
pgrmdesc = '''
Script d'installation. Execute des commandes, installe et désinstalle des paquets spécifiés dans 
le fichier : 
'''

pgrmdesc += installationFilePath

def log(text=os.linesep):
    ''' 
    Enregistrer dans le journal
    '''
    if os.path.isdir(logRoot) == False:
        os.makedirs(logRoot)
        
    with open(logName, "a+") as outfile:
        outfile.write(text + os.linesep)

def printTitle(text):
    ''' 
    Afficher une ligne soulignée à l'écran et dans le journal 
    '''
    
    # souligner le texte
    dashLine = ""
    for c in text:
        dashLine += "-"
    
    # affichage ecran
    print 
    print text
    print dashLine
    
    # affichage journal
    log()
    log(text)
    log(dashLine)
    
    
def printLine(text):
    ''' 
    Afficher une ligne à l'écran et dans le journal
    '''
    
    # affichage ecran
    print 
    print text
    
    # affichage journal
    log()
    log(text)
    
def exitProgram(code, text=""):
    printLine(text)
    exit(code)
    
def loggedCommand(text):
    ''' 
    Exécuter une commande et rediriger ses sorties vers le journal
    '''
    log("Command: " + text)
    with open(logName, "a+") as outfile:
        try:
            subprocess.call(shlex.split(text), stdout=outfile, stderr=outfile)
        except Exception as e:
            log("Erreur: " + str(e))
        except OSError as e:
            log("Erreur: " + str(e))

def parseInstallationFile():
    return json.load(open(installationFilePath))


if __name__ == "__main__":
    
    # parser les arguments
    parser = argparse.ArgumentParser(description=pgrmdesc)
   
    # lancement de l'installation
    parser.add_argument("-i", "--install",
                        action="store_true",
                        help="lancer le script")
    
    # editer le fichier d'installation
    parser.add_argument("-e", "--edit",
                        action="store_true",
                        help="editer le fichier d'installation")
    
    # ajout de paquet pour installation
    parser.add_argument("-ai", "--append-packet-to-install",
                        action="store_true",
                        help="ajouter un paquet à installer")
    
    # ajout de paquet pour desinstallation
    parser.add_argument("-au", "--append-packet-to-uninstall",
                        action="store_true",
                        help="ajouter un paquet à désinstaller")
    
    # affichage
    parser.add_argument("-d", "--display",
                        action="store_true",
                        help="montrer les commandes et paquets du fichier")
    
    # récupérer les arguments et les mots clefs
    knownArgs, otherArgs = parser.parse_known_args()
    
    if knownArgs.edit :
        subprocess.call(shlex.split("vim " + installationFilePath))
        exitProgram(0)
        
    if knownArgs.display:
        # parser le fichier de données
        try:
            data = parseInstallationFile()
        except Exception as e:
            exitProgram(1, "Fichier de données incorrect: " + str(e))

        for groupId, label in readableNames.items():
            print
            print(label + ":")
            print
            i = 0
            for e in data[groupId]:
                print("\t#" + str(i) + ": " + e)
                i += 1 
                
        # fin
        exitProgram(0)
    
    if knownArgs.append_packet_to_install or knownArgs.append_packet_to_uninstall:
        
        # verifier le nombre de paquets
        if(len(otherArgs) < 1):
            exitProgram(1, "Vous devez spécifier un ou plusieurs paquets à ajouter à la liste de paquets.")
        
        # parser le fichier de données
        try:
            data = parseInstallationFile()
        except Exception as e:
            exitProgram(1, "Fichier de données incorrect: " + str(e))

        # ajout a la liste correspondante
        if knownArgs.append_packet_to_install:
            listId = toInstallId
        if knownArgs.append_packet_to_uninstall:
            listId = toUninstallId
    
        for p in otherArgs:
            data[listId].append(p)

        # ecriture du fichier
        try:
            jsonfile = open(installationFilePath, "w")
            jsonfile.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
        except:
            exitProgram(1, "Impossible d'écrire le fichier: " + installationFilePath)
            
        # fin
        exitProgram(0, "Paquet ajouté avec succés.")

    # pas d'installation demandée: erreur
    if knownArgs.install == False:
        print("Vous devez spécifier des arguments ou des mots clefs.")
        print
        parser.print_help()
        exitProgram(1)
    
    # charger le fichier d'installation
    try:
        data = parseInstallationFile()
    except Exception as e:
        exitProgram(1, "Fichier de données incorrect: " + str(e))
   
    beforeCmds = data[beforeCommandsId]
    afterCmds = data[afterCommandsId]
    toInstall = data[toInstallId]
    toUninstall = data[toUninstallId]
   
    # execution
    printTitle("Installation: Commandes préliminaires: ")
    for i, c in enumerate(data[beforeCommandsId]):
        printLine("#" + str(i) + " " + c)
        loggedCommand(c)
                      
    printTitle("Installation: Desinstallation de paquets: ")
    for i, p in enumerate(data[toUninstallId]):
        printLine("#" + str(i) + " " + p)
        loggedCommand("sudo apt-get -y autoremove " + p)
        
    printTitle("Installation: Installation de paquets")
    for i, p in enumerate(data[toInstallId]):
        printLine("#" + str(i) + " " + p)
        loggedCommand("sudo apt-get -y install " + p)
    
    printTitle("Installation: Commandes finales")
    for i, c in enumerate(data[afterCommandsId]):
        printLine("#" + str(i) + " " + c)
        loggedCommand(c)
      
    printLine("Installation: Fin du script, journal disponible: " + logName)
     
