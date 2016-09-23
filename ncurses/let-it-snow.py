#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Tutoriel sur Ncurse, bibliotheque d'affichage sur terminaux
# Source: https://docs.python.org/2/howto/curses.html

import time
import subprocess
import os
import sys
import thread

def playLetItSnow():
    letitsnow = os.path.join(
                         os.path.dirname(os.path.abspath(__file__)) 
                         ,"let-it-snow.wav");
    subprocess.call("mplayer " + letitsnow + "", shell=True)


# tout le script se déroule dans un try pour intercepter l'appui sur CTRL+C
try:
    
    # intiation de la bibliothèque
    import curses
    stdscr = curses.initscr()
    
    # Désactiver l'affichage des frappes 
    curses.noecho()
    
    # Recevoir les entrées même sans appui de la touche entrée
    curses.cbreak()
    
    # Caracteristiques aléatoires
    from random import randrange
    
    charsList = [" ", "*"]
    
    def getRandomChar():
        return charsList[randrange(0, len(charsList))]
    
    randomEffects = [
                     curses.COLOR_WHITE,
                     curses.A_STANDOUT,
                     curses.A_REVERSE,
                     ]
    
    def getRandomEffect():
        return  randomEffects[randrange(0, len(randomEffects))]

    try:
        thread.start_new_thread(playLetItSnow, ())
    except OSError:
        sys.exit(0)
        pass
     
    while True: 
        height,width = stdscr.getmaxyx()
        for y in range(0, height - 1):
            for x in range(0, width):
                try:
#                     stdscr.addstr(y, x,
#                                   getRandomChar(),
#                                   getRandomEffect())
                    stdscr.addstr(y, x,
                                  getRandomChar())
                                  
                except curses.error:
                    pass
        stdscr.refresh()
        time.sleep(0.2)
    
except KeyboardInterrupt:
    
    # Terminer un programme curse
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    
    # L'affichage est parfois perturbé après ncurse
    subprocess.call("reset")
    
    sys.exit(0)
        
