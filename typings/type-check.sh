#!/bin/bash

# dimanche 27 mai 2018, 20:06:46 (UTC+0200)

# /!\ /!\ MyPy check only typed objects, do not forget -> None

# /!\ With module option (-m), mypy check only files imported in __init__ file
# mypy -m src

mypy .
