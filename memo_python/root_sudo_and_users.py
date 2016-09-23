#!/usr/bin/python2.7
# encoding: utf-8
'''
Created on 7 janv. 2016

@author: remipassmoilesel
'''

import shlex
import getpass
import subprocess

print "This script was called by: " + getpass.getuser()

print "Now do something as 'root'..."
subprocess.call(shlex.split('sudo id -nu'))

print "Now switch back to the calling user: " + getpass.getuser()