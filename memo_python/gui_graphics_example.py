#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Source: http://www.tutorialspoint.com/python/python_gui_programming.htm
"""

import Tkinter

# créer une fenetre
window = Tkinter.Tk()

# créer un canvas
canvas = Tkinter.Canvas(window, bg="white", height=600, width=800)

canvas.pack()
window.mainloop()