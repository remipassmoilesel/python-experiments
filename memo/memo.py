#!/usr/bin/python2.7
# encoding: utf-8

import argparse
import datetime
import os
import re
from string import join
import subprocess

# flag de debogage
DEBUG = False;

# chemin du fichier de memo
MEMO_FILE_NAME = "memo.txt"
MEMO_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/" + MEMO_FILE_NAME

# description succincte du programme affichée dans l'aide
PGRM_DESC = '''
Utilitaire de conservation d'informations courtes. 
Filtre possible par catégorie.

Les informations sont enregistrées dans le fichier:
  
'''
PGRM_DESC += MEMO_FILE_PATH

# editeurs 
GRAPHICAL_EDITOR = "xdg-open"
CLI_EDITOR = "vim"

# catégorie par défaut
DEFAULT_CATEG = "default".lower()

# marque d'en tête
HEADER_MARK = "#"

# marque de catégorie
CATEG_MARK = "::"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def exitProgram(code=0, msg=""):
    """
    Arret du programme avec affichage éventuel de message
    """
    if msg != "":
        print(msg)
        
    exit(code)
    
def appendMemo(memo):
    """
    Ajoute un memo à 'path' et retourne vrai, ou faux en cas d'échec
    """
    try:
        inFile = open(MEMO_FILE_PATH, "a")
        inFile.write("\n")
        inFile.write(memo.writableRepresentation());
        return True
    except:
        return False
        

class MemoElement:
    
    def __init__(self, header, content, categ=""):
        self.header = header.strip()
        self.content = content.strip()
        self.categ = categ.strip().lower() if categ != None and categ != "" else DEFAULT_CATEG
    
    def __repr__(self):
        return self.displayableRepresentation();
    
    def displayableRepresentation(self):
        """
        Retourne une représentation du mémo affichable dans une console
        """
        output = bcolors.OKBLUE + HEADER_MARK + " "
        if self.categ != "" and self.categ != DEFAULT_CATEG:
            output += "[" + self.categ + "] "
        output += self.header + bcolors.ENDC + "\n" 
        output += self.content
        
        return output
        
    def writableRepresentation(self):
        """
        Retourne une représentation à écrire dans un fichier
        """
        output = "\n"
        output += HEADER_MARK + " "
        output += self.categ + " " + CATEG_MARK + " "
        output += self.header + " \n"
        output += "Ajouté le: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\n"
        output += self.content + "\n"
        
        return output;
        
    def getHeader(self):
        return self.header
    
    def getContent(self):
        return self.content
    
    def getCategory(self):
        return self.categ
    

class MemoContainer:
    """
    Conteneur de mémo
    """
    def __init__(self, path):
        self.path = path
        self.content = []
        self.load()
    
    def load(self):
        """
        Charge un fichier de memo
        """
        # verifier si le memo existe
        if os.path.isfile(self.path) == False:
            print("Le fichier de mémo n'existe pas.")
            try:
                inFile = open(self.path, "a")
                inFile.write("Memo" + os.linesep)
                inFile.write("----" + os.linesep + os.linesep)
                print("Il à été créé à l'emplacement: " + self.path)
            except:
                exitProgram(code=1, msg="Impossible de créer le mémo à l'emplacement: " + self.path)
                
        # charger le fichier 
        with open(self.path, "r") as inFile:
            
            # lire les lignes dans une variable
            lines = inFile.readlines()
            lines.append("##")

            if DEBUG:            
                print("Chargement du mémo: ")
                
            categ = ""
            header = ""
            content = ""
            # iterer les lignes
            for l in lines:

                matcher = re.match("^ *" + HEADER_MARK + " *(?:(.+)" + CATEG_MARK + ")? *(.+)", l)
                
                if DEBUG:
                    print("Ligne: '", l, "'")
                    print(matcher)
                
                # ligne d'entete
                if matcher:
                    i = 0
                    
                    if DEBUG:
                        for i, val in enumerate(matcher.groups()):
                            print(i , " ", val)
                    
                    # creer un nouvel element et le conserver
                    if header != "" and content != "":
                        self.content.append(MemoElement(header, content, categ))
                    
                    
                    # recuperer l'entete du prochain, avec ou sans categorie
                    if matcher.groups() > 2:
                        categ = matcher.group(1)
                        header = matcher.group(2)
                    else:
                        categ = ""
                        header = matcher.group(1)
                    
                    # vider le contenu stocké
                    content = ""
                    
                # autres lignes: ajouter les lignes non vides au contenu 
                elif re.search("\\w+", l):
                    
                    if DEBUG:
                        print('Ajouté au contenu')
                    
                    content += l
                    
                    
    def search(self, keywords, categ=None):
        """
        Retourne un liste d'objets correspondant aux mots clef
        """
        
        # le résultat à renvoyer
        rslt = [];

        # la position du dernier en-tete
        if DEBUG:
            print("keywords")
            print(keywords)
        
        # créer une regex
        regexa = [] 
        for w in keywords:
            regexa.append(re.sub("[^a-z]", ".?", w, re.IGNORECASE))
            
        regex = "(" + join(regexa, "|") + ")+"
        
        # categorie de recherche
        categ = categ.strip().lower() if categ != None else ""
        
        # analyser les elements de memos
        for memo in self.content:
            
            # comparaison de la catégorie 
            if categ != "" and memo.getCategory() != categ:
                continue
            
            # comparaison des mots clefs
            inHeader = re.search(regex, memo.getHeader(), re.IGNORECASE)
            inContent = re.search(regex, memo.getContent(), re.IGNORECASE)
            inCateg = re.search(regex, memo.getCategory(), re.IGNORECASE)
            
            if inHeader or inContent or inCateg:
                rslt.append(memo)
        
        return rslt
    
    def getContent(self, categ=""):
        
        if categ == None or categ == "":
            return self.content
        
        # tri par catégorie
        else :
            categ = categ.strip().lower()
            output = [];
            for memo in self.content:
                if memo.getCategory() == categ:
                    output.append(memo)
                    
            return output


if __name__ == "__main__":
    
    # parser les arguments
    parser = argparse.ArgumentParser(description=PGRM_DESC)
   
    # rechercher
    parser.add_argument("-s", "--search",
                        action="store_true",
                        help="rechercher dans le fichier de mémo")
    
    # filtre de categorie
    parser.add_argument("-c", "--category",
                        help="indiquer un filtre de catégorie")
    
    # afficher les categories
    parser.add_argument("-l", "--listcategory",
                        action="store_true",
                        help="afficher les catégories disponibles")
    
    # ajout de memo
    parser.add_argument("-a", "--append",
                        action="store_true",
                        help="ajouter un mémo: ['catégorie'] 'en-tête' 'contenu'")
   
    # edition du memo
    parser.add_argument("-e", "--edit",
                        action="store_true",
                        help="editer le fichier de memo")
    
    # utiliser un editeur graphique 
    parser.add_argument("-g", "--graphicaleditor",
                        action="store_true",
                        help="utiliser un éditeur graphique")
    
    # afficher tout
    parser.add_argument("-d", "--display",
                        action="store_true",
                        help="afficher l'intégralité du fichier")
    
    
    # récupérer les arguments et les mots clefs
    knownArgs, unkArgs = parser.parse_known_args()
    
    # affichage pour debuggage
    if DEBUG:
        print("knownArgs: ")
        print(knownArgs)
        print("unkArgs: ")
        print(unkArgs)
        print("")
    
    # argument "edit" spécifié, ouvrir le fichier de memo avec vim puis quitter
    if knownArgs.edit or knownArgs.graphicaleditor:
        
        # déterminer l'editeur a utiliser
        editor = GRAPHICAL_EDITOR if knownArgs.graphicaleditor == True else CLI_EDITOR
        
        # commande d'edition
        subprocess.call(editor + " " + MEMO_FILE_PATH, shell=True)
        
        exitProgram()
       
    # argument "append" spécifié, ajouter un memo
    if knownArgs.append :
        
        # verifier le nombre d'argument
        if len(unkArgs) < 2:
            exitProgram(1, "Erreur: vous devez spécifier un en-tête et un contenu pour ajouter un memo")
        
        # verifier la taille des arguments
        for i, val in enumerate(unkArgs):
            if len(val) < 1:
                exitProgram(1, "Erreur: vous ne devez pas spécifier d'argumnts vides")
                
        memo = None;            
        # créer un memo avec categorie     
        if len(unkArgs) > 2:
            memo = MemoElement(header=unkArgs[1], content=unkArgs[2], categ=unkArgs[0])
        # ou sans categorie
        else:
            memo = MemoElement(header=unkArgs[0], content=unkArgs[1])
            
        # ecriture et sortie
        success = appendMemo(memo)
            
        if success:
            exitProgram(0, "Mémo ajouté avec succés.")
        else:
            exitProgram(1, "Erreur lors de l'ajout du mémo au fichier: " + MEMO_FILE_PATH)

    # argument "display_all" spécifié
    if knownArgs.display :
        
        # charger le conteneur 
        memoCtr = MemoContainer(MEMO_FILE_PATH)
        
        print("")
        
        # categorie d'affichage
        if knownArgs.category:
            print(bcolors.OKGREEN + "Affichage restreint à la catégorie: \"" + knownArgs.category + "\"" + bcolors.ENDC)
            print("")
        
        # afficher les mémo
        for memo in memoCtr.getContent(knownArgs.category):
            print(memo) 
            print("")
        
        # quitter
        exitProgram(0)
        
    # argument "search" spécifié
    if knownArgs.search :
        
        # si pas d'arguments et pas de mot-clefs spécifiés, aide puis arret    
        if len(unkArgs) < 1:
            print("Commande incorrecte.")
            print("")
            parser.print_help()
            exitProgram(1)
            
        # charger le memo
        memo = MemoContainer(MEMO_FILE_PATH)
        
        print("")
        
        # categorie de recherche
        if knownArgs.category:
            print(bcolors.OKGREEN + "Recherche restreinte à la catégorie: \"" + knownArgs.category + "\"" + bcolors.ENDC)
        
        # rechercher les elements
        elements = memo.search(unkArgs, knownArgs.category)
        
        # affichage
        keywordsStr = ",".join(unkArgs)
        
        # pas de résultat
        if len(elements) == 0:
            print("Aucun mémo ne correspond aux mots clefs: \"" + keywordsStr + "\"")
    
        # affichage des résultats
        else:
            print("Mémos correspondant aux mots clefs \"" + keywordsStr + "\":") 
            print("")
    
            for m in elements:
                print(str(m))
                print("")
                
        exitProgram(0);
        
    # argument "listcategory" spécifié 
    if knownArgs.listcategory :
        
        # charger le conteneur 
        memoCtr = MemoContainer(MEMO_FILE_PATH)
        
        print("")
        print("Catégories: ")
        print("")
        
        # extraire les catégories
        categories = {}
        for memo in memoCtr.getContent():
            cat = memo.getCategory()
            val = categories.get(cat)
            val = val if val != None else 0
            categories[cat] = val + 1;

        # largeur de colonne
        colLen = 25;
        
        # affichage
        for i, cat in enumerate(categories):
            spaces = "";
            for i in range(colLen - len(cat)):
                spaces += " ";
                
            print cat + spaces + " (" + str(categories[cat]) + ")";
        
        # quitter
        exitProgram(0)
        
        
    # aucun commande spécifiée
    print("Commande incorrecte.")
    print("")
    parser.print_help()
    exitProgram(1)
    
