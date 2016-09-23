#!/usr/bin/python2.7
# encoding: utf-8


from node import *

if __name__ == "__main__":
    
    # Test de a méthode feuille
    assert(Node("test").isLeaf() == True)
    
    print "Arbre du TD 17 d'algo, exercice 2"
    tree1 = Node("*", Node("-", Node("u"), Node("^", Node("+", Node("x"), Node("*", Node("y"), Node("log", Node("-", Node("z"), Node("5"))))), Node("3"))), Node("2"))
    print tree1
 
    TreeWindow(tree1).show()
 
#     print node
#     
#     import sys
#     def prefixDisplayTree(node):
#         """
#         Affichage prefixé d'un arbre 
#         """
#         sys.stdout.write(node.getValue())
#         
#         if node.isLeaf() == False:
#             for s in node:
#                 prefixDisplayTree(s) 
#     
#     prefixDisplayTree(node)
#     
    