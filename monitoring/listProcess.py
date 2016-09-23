#!/usr/bin/python2.7
# encoding: utf-8

import os, re

class LinuxProcess:
    """
    Représentation d'un processus linux
    """
    
    def __init__(self, pid):
        self.values = {}
        self.pid = pid
        self.lineRegex = '^\s*([a-z0-9_-]+)\s*:\s*(.+)\s*$'
        
    def parseStatusLine(self, line):
        """
        Analyser une ligne de fichier 'status' de processus
        """
        m = re.search(self.lineRegex, line, re.IGNORECASE)
        if m != None:
            self.addEntry(m.group(1), m.group(2))
        else:
            raise Exception("Invalid line")
        
    def addEntry(self, key, value):
        """
        Ajouter une entrée dans les caractéristiques du processus
        """
        self.values[key] = value

    def getValue(self, key):
        return self.values[key]

    def __repr__(self):
        return "Processus: " + str(self.pid) + ", Nom: " + self.getValue("Name")

    @staticmethod
    def listAllProcess():
        """
        Liste les processus actif et retourne une liste d'objets 
        """
    
    
        # la racine ou seront analysés les processus
        procRoot = '/proc'
        
        # la sortie
        output = []
        
        # itérer les processus actifs
        for pid in os.listdir(procRoot):
            
            # ne traiter que les noms de processus sous forme de chiffre
            if pid.isdigit():
                
                # créer une représentation de processus
                processList = LinuxProcess(int(pid))
                
                try:
                    # ouvrir le fichier de statut et itérer les lignes
                    statusFile = open(os.path.join(procRoot, pid, 'status'), 'r')
                    for line in statusFile:
                        try:
                            processList.parseStatusLine(line)
                        except:
                            print "Ligne ignorée: " + line
                        
                    output.append(processList)
                        
                except IOError: 
                    print "Processus ignoré: " + pid
                    continue
                
        return output
    

if __name__ == "__main__":
    
    processList = LinuxProcess.listAllProcess();
    
    i = 0
    for cat in processList:
        print str(i) + " " + str(cat)
        i+=1
        

