#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import subprocess

import sys

scriptDir = os.path.dirname(os.path.realpath(__file__))
sourceRoot = os.path.join(scriptDir, 'python-project-dir')
mainPy = os.path.join(sourceRoot, 'main.py')

pythonInterpreter = os.path.join(sourceRoot, '.venv/bin/python3.6')

installVenv = os.path.join(sourceRoot, 'install-venv.sh')
activateVenvPath = os.path.join(sourceRoot, '.venv/bin/activate')


def checkPrerequisites():
    assert os.path.isdir(sourceRoot), 'Source root path is incorrect: ' + sourceRoot
    assert os.path.isfile(installVenv), 'Virtual environment script path is incorrect: ' + installVenv
    assert os.path.isfile(mainPy), 'Main script path is incorrect: ' + mainPy


def checkPythonVirtualEnv():
    if os.path.isfile(pythonInterpreter) is False:
        subprocess.run(installVenv, shell=True, cwd=sourceRoot)


def executeCommand():
    command = mainPy + ' ' + ' '.join(sys.argv[1:])

    currentVenv: str = os.getenv('VIRTUAL_ENV')
    if currentVenv is None or currentVenv.endswith('python-project-dir/.venv') is False:
        command = "source " + activateVenvPath + " && " + command

    result = subprocess.run(command, shell=True, executable="/bin/bash")
    exit(result.returncode)


if __name__ == '__main__':
    checkPrerequisites()
    checkPythonVirtualEnv()
    executeCommand()
