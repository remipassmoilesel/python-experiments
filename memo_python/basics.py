# encoding: utf-8
'''
Created on 7 janv. 2016

@author: remipassmoilesel
'''

import random

random.randint(1, 10)

class MemoElement:
    
    def __init__(self, header, content):
        
        # enlever les sauts de ligne superflus
        if header[-1:] == "\n":
            header = header[:-1]
        
        if content[-1:] == "\n":
            content = content[:-1]
        
        self.header = header
        self.content = content
    
    def __str__(self):
        return self.header + " " + self.content
     
    def __repr__(self):
        return self.header + "\n" + self.content
        
    def getHeader(self):
        return self.header


# conversion en entiers
a = int("8")

# itérer une liste
testList = []
for i, val in enumerate(testList):
    print(i, val)
    
# iterer un tableau, a verifier
arrayTest = ["hello", "world"]
for i, val in arrayTest:
    print(i, val)

# verifier si une clef est dans un dict
dict1 = {"a" : 1, "b" : 2 }
if "a" in dict1:
    print "vrai"

# itérer des caractères
for c in "string":
    print(c)
    
# try catch

try:
    print "Something"
except:
    # ne rien faire en cas d'erreur
    pass

try:
    print("Hello")
except ZeroDivisionError as e:
    print("Erreur: ", e)
finally:
    print("Finnaly")

# afficher les erreurs
import traceback
traceback.print_exc()
    
# parametres optionnels ou variables
def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les
    paramètres nommés dans un dictionnaire"""
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))
    
fonction_inconnue(salut="ca va?")

