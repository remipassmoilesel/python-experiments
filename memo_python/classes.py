# encoding: utf-8
'''
Created on 7 janv. 2016

@author: remipassmoilesel
'''

class Personne: # Définition de notre classe Personne
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""
    def __init__(self): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = "Dupont"

    def __fakePrivateMethod(self): # Méthode privée pas vraiment privée ...
        self.var = "val"