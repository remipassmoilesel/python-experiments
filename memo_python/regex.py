'''
Created on 11 févr. 2016

@author: remipassmoilesel
'''

import re

# extraire un groupe
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)

if m.groups() > 2:
    print "somtething";

# recherche sans casse 
m = re.search('(?<=abc)def', 'abcdef', re.IGNORECASE)
