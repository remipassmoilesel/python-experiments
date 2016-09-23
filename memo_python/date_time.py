# encoding: utf-8
'''
Created on 7 janv. 2016

@author: remipassmoilesel
'''

import datetime

# ajouter 10 minutes
now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 10)

# jour
today = datetime.date.today()
print today.strftime('We are the %d %m %Y') 

# jour + heures
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# comparaison de dates
past = datetime.datetime.now()
present = datetime.datetime.now()

print past < present  # True
print datetime(3000, 1, 1) < present  # False

# parser une date
datetime.datetime.strptime("2015-10-12", "%Y-%m-%d")

u = datetime.datetime.strptime("2011-01-01", "%Y-%m-%d")
d = datetime.timedelta(days=21)
t = u + d





