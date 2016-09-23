'''
Created on 12 janv. 2016

@author: remipassmoilesel
'''
# voir https://docs.python.org/2/howto/curses.html

import curses

stdscr = curses.initscr()

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

stdscr.addstr(0, 0, "Current mode: Typing mode",
              curses.A_REVERSE)
stdscr.refresh()