#!/bin/bash

# mardi 1 mai 2018, 22:29:51 (UTC+0200)

set -x
set -e

mypy **/*.py

green -p '*Test.py'
