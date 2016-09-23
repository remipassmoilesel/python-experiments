#!/usr/bin/python2.7
# encoding: utf-8

import json

list1 = [1, 2, (3, 4)]  # Note that the 3rd element is a tuple (3, 4)
print json.dumps(list1)  # '[1, 2, [3, 4]]'
print json.dumps(list1, sort_keys=True, indent=4, separators=(',', ': '));

print json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

operation = '''
{
    "install" : [
         "packet1",
         "packet2",
         "packet3",
         "packet4"
    ],
    
    "uninstall" : [
         "packet1",
         "packet2",
         "packet3",
         "packet4"
    ],
    
    "commands" : [
         "cmd1",
         "cmd2",
         "cmd3",
         "cmd4"
    ]
}
''' 

var = json.loads(operation)

for i, cat in enumerate(var):
    print str(i) + " " + cat
    for i2, p in enumerate(var[cat]):
        print str(i2) + " " + p
        
        
with open('data.json') as data_file:    
    data = json.load(data_file)



