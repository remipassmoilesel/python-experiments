#!/usr/bin/python2.7
# encoding: utf-8

# lire les lignes de plusieurs fichiers

import fileinput, glob, string, sys

for line in fileinput.input(glob.glob("./*")):
    if fileinput.isfirstline(): # first in a file?
        sys.stderr.write("-- reading %s --\n" % fileinput.filename())
        
    sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))