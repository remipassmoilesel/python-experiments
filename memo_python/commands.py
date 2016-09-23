# encoding: utf-8
'''
Created on 7 janv. 2016

@author: remipassmoilesel
'''
import subprocess
import shlex
import os
import datetime

# pas d'interaction possible
output = subprocess.check_output("cat file > test", shell=True)

def command(text):
    return subprocess.call(shlex.split(text))

 # conserver l'heure de l'appel
date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
logName = "installation_" + date + ".txt"

def loggedCommand(text):
    with open(logName, "a+") as outfile:
        subprocess.call(shlex.split(text), stdout=outfile, stderr=outfile)

output = subprocess.call("cat file | less", shell=True)
