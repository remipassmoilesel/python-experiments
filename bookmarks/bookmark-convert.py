#!/usr/bin/python2.7
# encoding: utf-8

import csv

pattern = '<DT><A HREF="%link%">%description%</A>'

with open('resources.csv', 'rb') as csvfile:
    linkreader = csv.reader(csvfile, delimiter=',')
    for row in linkreader:
        link = row[1]
        description = row[0]

        if link and description:
            line = pattern.replace("%link%", link)
            line = line.replace("%description%", description)
            print line
