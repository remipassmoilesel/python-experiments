'''
Created on 12 févr. 2016

@author: remipassmoilesel
'''

# conversion en chaines
print "String concatenated to " + str(12)

print len("Taille de la chaine")

# joindre un tableau
arrayTest = ["hello", "world"]
print join(arrayTest, ", ")

# equivalent de trim
s = "  \t a string example\t  "
s = s.strip()
s = s.strip(' \t\n\r')