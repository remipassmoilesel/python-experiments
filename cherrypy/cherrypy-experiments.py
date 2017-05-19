#!/usr/bin/env python3

import cherrypy 
import random
import os
import os.path
import string
import sqlite3

DB_STRING = "credentials.db"

def setupDatabase():
    with sqlite3.connect(DB_STRING) as con: 
        con.execute("CREATE TABLE credentials (time, value)")

class Portal(object): 

    @cherrypy.expose
    def index(self):
        return open('public/index.html')
    
    @cherrypy.expose 
    def submit(self, strig=""): 
        return ''.join(random.sample(string.hexdigits, 8))
    
if __name__ == '__main__':

    conf = { 
            '/': { 
                'tools.sessions.on': True, 
                'tools.staticdir.root': os.path.abspath(os.getcwd()) 
                }, 
            '/static': { 
                'tools.staticdir.on': True, 
                'tools.staticdir.dir': './public' 
                } 
            } 
    cherrypy.quickstart(Portal(), '/', conf) 
