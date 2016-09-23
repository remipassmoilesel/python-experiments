'''
Created on 10 janv. 2016

@author: remipassmoilesel
'''

import xml.etree.ElementTree as ET
e = ET.parse('thefile.xml').getroot()

for atype in e.findall('type'):
    print(atype.get('foobar'))

root = ET.parse('country_data.xml')
root = root.getroot()

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

root.write('output.xml')

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)