#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Tutoriel sur Ncurse, bibliotheque d'affichage sur terminaux
# Source: https://docs.python.org/2/howto/curses.html

import time
import subprocess
import sys

# tout le script se déroule dans un try pour intercepter l'appui sur CTRL+C
try:
    
    # intiation de la bibliothèque
    import curses
    stdscr = curses.initscr()
    
    # Désactiver l'affichage des frappes 
    curses.noecho()
    
    # Recevoir les entrées même sans appui de la touche entrée
    curses.cbreak()
    
    # creer une fenêtre
    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    
    # creer un pad, un type spécial de fenetre qui peut être plus grande que l'écran
    pad = curses.newpad(100, 100)
    
    # Affichage de caracteres aleatoires
    for y in range(0, 100):
        for x in range(0, 100):
            try:
                pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
            except curses.error:
                pass
    
    
    #  Displays a section of the pad in the middle of the screen
    pad.refresh(0,0, 5,5, 20,75)
    
    # 
    
    from random import randrange
    
    charsList = [" "]
    
    def getRandomChar():
        return charsList[randrange(0, len(charsList))]
    
    randomEffects = [
                     curses.COLOR_WHITE,
                     curses.A_STANDOUT,
                     curses.A_REVERSE,
                     ]
    
    def getRandomEffect():
        return  randomEffects[randrange(0, len(randomEffects))]
    
    while True: 
        for y in range(0, 100):
            for x in range(0, 100):
                try:
                    stdscr.addstr(y, x,
                                  getRandomChar(),
                                  getRandomEffect())
                    #pad.addch(y,x,  getRandomChar(), curses.A_BLINK)
                except curses.error:
                    pass
        #pad.refresh(0,0, 5,5, 20,75)
        stdscr.refresh()
        time.sleep(0.2)
    
except KeyboardInterrupt:
    
    # Terminer un programme curse
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    
    # L'affichage est parfois perturbé après ncurse
    subprocess.call("reset")
    
    sys.exit(0)
        