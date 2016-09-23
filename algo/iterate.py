#!/usr/bin/python2.7
# encoding: utf-8

from node import *

print "Arbre du TD 17 d'algo, exercice 2"
tree1 = Node("*", 
            Node("-", 
                 Node("u"), Node("^", 
                                 Node("+", 
                                    Node("x"), Node("*", 
                                                    Node("y"), Node("log", 
                                                                    Node("-", 
                                                                         Node("z"), Node("5"))))), 
                                 Node("3"))), 
             Node("2"))

# parcours
processed = []

n = tree1
while n.value != "y":
    processed.append(n)
    
    print n.value
    
    if n.getChild(0) != None and n.getChild(0) not in processed:
        n = n.getChild(0)
        
    elif n.getChild(1) != None and n.getChild(1) not in processed:
        n = n.getChild(1)
        
    elif n.father != None and n.father not in processed:
        n = n.father
        
    else:
        break
    ap
print n

