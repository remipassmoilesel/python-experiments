# encoding: utf-8
'''
Created on 7 janv. 2016

@author: remipassmoilesel
'''

#  creer une liste
stringList = ["hello", "world"]

# ajouter un elemenrt
stringList.append("!")

#  taille de la liste
len(stringList)

for i, val in enumerate(stringList):
    print i, val
    
mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire["pseudo"] = "6pri1"

fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items():
    print("La clé {} contient la valeur {}.".format(cle, valeur))

# dictionnaires:  extraire les catégories
categories = {}
for memo in memoCtr.getContent():
    cat = memo.getCategory()
    val = categories.get(cat)
    val = val if val != None else 0
    categories[cat] = val + 1;
