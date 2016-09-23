#!/usr/bin/python2.7
# encoding: utf-8

import datetime
import subprocess

class C: 
    """ 
    Commandes chainées. Permet d'éxécuter une suite de commandes Unix à la suite les unes des 
    autres, journalisées dans un fichier texte dont le nom est défini dans le constructeur. 
    """
    
    def __init__(self, logName=None):
        
        # date/heure de lancement de la commande 
        self.launchDate = self._getDate();
        
        # nom du journal de commande
        if logName == None:
            self.logName = self.launchDate
        else :
            self.logName = logName
            
    def c(self, command, logLine=None):
        """ Executer une commande Unix journalisée. Retourne l'objet executeur, ce qui permet d'écéxuter
        une nouvelle commande à la suite. """
        
        with open(self.logName, "a+") as outfile:
            
            # flusher après chaque sortie ou le fichier de journal paraitra en désordre

            # ouvrir le journal
            outfile.write("\n#c# " + self._getDate() + ": " + command + "\n")
            outfile.flush()
            
            # ecrire la ligne supplémentaire optionnelle
            if logLine != None:
                outfile.write(logLine + "\n")
                outfile.flush()
            
            # éxécuter la commande
            subprocess.call(command, stdout=outfile, stderr=outfile, shell=True)
            outfile.flush()
            
        return self
    
    def executeAll(self, commandList):
        for i, comm in enumerate(commandList):
            self.c(comm, "Commande " + str(i) + " / " + str(len(commandList)))
    
    def _getDate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    

if __name__ == "__main__":
    C("firstLog").c("ls").c("mkdir test").c("cd test").c("touch test2").c("cd ..").c("ls")
    
    C("firstLog").executeAll(["mkdir test2", "cd test2", "ls"])
    
