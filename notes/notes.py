#!/usr/bin/python2.7
# encoding: utf-8

import re
import os
import argparse
import subprocess
import datetime
import shutil
from string import join

# Turn to true to verbose output
DEBUG = False;

def log(msg):
    """ Log message only if debug mode is turn on """
    if DEBUG:
        print msg


# Line number to display when list notes
linesDisplayedWhenList = 3

# Editors
GRAPHICAL_EDITOR = "xdg-open"
CLI_EDITOR = "vim"

# Repository path
notesRepName = "notes-repository"
notesRepPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), notesRepName)
log("Repository path: " + notesRepPath);

# notes prefix
noteNamePrefix = "note_"
noteExtension = "md"

# template path
noteTemplateName = "template.md"
noteTemplatePath = os.path.join(notesRepPath, noteTemplateName)

log("Template path: " + noteTemplatePath);

# datetime to add to a new note name
today = datetime.datetime.now()

# small help to display
PGRM_DESC = '''
Small utility to save notes.
Notes are saved in:
'''
PGRM_DESC += notesRepPath


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def exitProgram(code=0, msg=""):
    """
    Stop program
    """
    if msg != "":
        print msg

    exit(code)


def displayNote(notePath, lineMax=None):
    """
    Display a note, without first blank lines
    """
    print(bcolors.OKGREEN + "@ Numéro de la note: " + str(
        listNotesPaths().index(notePath)) + bcolors.ENDC)
    print("@ Nom de la note: " + notePath.split(os.sep)[-1])
    print("@ Chemin: " + notePath)
    print("")

    i = 0
    firstPrinted = False
    for line in getLinesFromNote(notePath):

        # avoid printing first empty lines
        if firstPrinted is not True and re.search("[a-z0-9]+", line, re.IGNORECASE) is None:
            continue
        else:
            firstPrinted = True

        # first line; print in color. [0:-1] print without end of line
        if i == 0:
            print(bcolors.OKBLUE + bcolors.UNDERLINE + line[0:-1] + bcolors.ENDC)
        # otherwise print normally
        else:
            print(line[0:-1])

        if lineMax != None and i > lineMax:
            break;

        i += 1

    if i == 0:
        print "Note is empty"

    print


def resolveNoteName(data):
    """
    Try to resolve a note name regardless it is a note name, partial name or number.
    Return None if nothing is found
    """
    # arg is a full path
    if os.path.isfile(data) == True:
        return data;

    # arg is a note number
    if re.search("^[0-9]*$", data):
        notes = listNotesPaths()
        if int(data) < len(notes):
            return notes[int(data)]

    # arg is a relative path or a partial name
    if len(data.split(os.sep)) < 2:

        # relative path: return absolute path
        notePath = os.path.join(notesRepPath, data)
        if os.path.isfile(notePath):
            return notePath

        # partial name: search
        for path in listNotesPaths():
            if re.search(data, path, re.IGNORECASE) is not None:
                return path

    # nothing found
    return None


def getLinesFromNote(notePath):
    """
    Return all lines from a note
    """

    try:
        f = open(notePath)
        output = f.readlines()
    except:
        exitProgram(1, "Impossible de lire le fichier: " + notePath)

    return output


def listNotesPaths():
    """
    Return an ordered list of note paths
    """

    output = [];

    # lister un répertoire
    dirList = os.listdir(notesRepPath)

    # ajouter les fichier utiles
    for fname in dirList:
        if fname != "." and fname != ".." and fname != noteTemplateName:
            output.append(os.path.join(notesRepPath, fname))

    # trier la liste
    output.sort()

    # retourner la liste
    return output


def editNote(notePath, useGraphicalEditor=False):
    """
    Edit a note, with graphical or non graphical editor
    """
    # choose editor
    editor = GRAPHICAL_EDITOR if useGraphicalEditor == True else CLI_EDITOR

    # call editor
    subprocess.call(editor + " " + notePath, shell=True)


def createNewNote(suffix=None):
    """
    Create a new note and return its full path
    """

    # generate note name
    newNoteName = noteNamePrefix + today.strftime('%Y-%m-%d_%H-%M-%S')
    if suffix != None:
        newNoteName += "_" + suffix
    newNoteName += "." + noteExtension

    newNotePath = os.path.join(notesRepPath, newNoteName)

    # create file from template
    try:
        shutil.copy(noteTemplatePath, newNotePath)
    except:
        exitProgram(1, "Unable to create note here: " + newNotePath)

    # return full path
    return newNotePath


def checkNoteRepository():
    """
    Check if repository and templates exist, or try to create them
    """
    # check folders
    if os.path.isdir(notesRepPath) == False:
        try:
            os.makedirs(notesRepPath)
            print(
                "Note repository was created here: " + notesRepPath)
        except:
            exitProgram(1, "Unable to create note repository: " + notesRepPath)

    # check note template
    if os.path.isfile(noteTemplatePath) == False:
        try:
            open(noteTemplatePath, 'a').close()
        except:
            exitProgram(1,
                        "Unable to create note template here: " + noteTemplatePath)


if __name__ == "__main__":

    # check repo
    checkNoteRepository()

    # parse arguments
    parser = argparse.ArgumentParser(description=PGRM_DESC)

    parser.add_argument("-n", "--newnote",
                        action="store_true",
                        help="create a new note")

    parser.add_argument("-e", "--editnote",
                        action="store_true",
                        help="edit exisiting note")

    parser.add_argument("-s", "--search",
                        action="store_true",
                        help="search in all notes")

    parser.add_argument("-t", "--edittemplate",
                        action="store_true",
                        help="edit template")

    parser.add_argument("-l", "--list",
                        action="store_true",
                        help="list all notes")

    parser.add_argument("-d", "--display",
                        action="store_true",
                        help="display a note")

    parser.add_argument("-a", "--displayall",
                        action="store_true",
                        help="display all notes")

    parser.add_argument("-g", "--graphicaleditor",
                        action="store_true",
                        help="use graphical editor")

    knownArgs, unkArgs = parser.parse_known_args()

    log("knownArgs: ")
    log(knownArgs)
    log("unkArgs: ")
    log(unkArgs)

    # create new note
    if knownArgs.newnote:

        if len(unkArgs) > 0:
            notename = createNewNote(unkArgs[0])
        else:
            notename = createNewNote()

        # create note
        print("This note have been created: " + notename)

        # then edit it
        editNote(notename, knownArgs.graphicaleditor)

        exitProgram()

    # edit existing note
    if knownArgs.editnote:

        # check if exist
        if len(unkArgs) != 1:
            exitProgram(1, "You must specify a name, a partial name or a number.")

        # get path of note
        notePath = resolveNoteName(unkArgs[0])

        # not found
        if notePath == None:
            exitProgram(1, "Unable to found note: " + unkArgs[0])

        # edit it
        editNote(notePath, knownArgs.graphicaleditor)

        exitProgram()

    # edit template
    if knownArgs.edittemplate:
        editNote(noteTemplatePath, knownArgs.graphical_editor)

        exitProgram()

    # list existing notes
    if knownArgs.list:

        notePaths = listNotesPaths()
        if len(notePaths) < 1:
            exit(0, "No notes available in: " + notesRepPath)

        # iterate notes and display them
        i = 0
        for noteName in notePaths:
            displayNote(noteName, linesDisplayedWhenList)

        exitProgram()

    # display note
    if knownArgs.display:

        # check if exist
        if len(unkArgs) != 1:
            exitProgram(1, "You must specify a name, a partial name or a number.")

        # get full path
        notePath = resolveNoteName(unkArgs[0])

        # not found
        if notePath == None:
            exitProgram(1, "Unable to found note: " + unkArgs[0])

        # display
        displayNote(notePath)

        exitProgram()

    # display all
    if knownArgs.displayall:

        print("Notes from directory: " + notesRepPath)
        print("")

        for path in listNotesPaths():
            displayNote(path)

        exitProgram()

    # search in notes
    if knownArgs.search:

        # check keywords
        if len(unkArgs) < 1:
            exitProgram(1, "You must specify keywords.")

        print("Notes from directory: " + notesRepPath)
        print("")

        # créer une regex de recherche
        regexa = []
        for w in unkArgs:
            regexa.append(re.sub("[^a-z]", ".?", w, re.IGNORECASE))

        regex = "(" + join(regexa, "|") + ")+"

        log("searching notes: regex: " + regex)

        # iterate notes and search keywords
        i = 0
        for path in listNotesPaths():

            with open(path, 'r') as cfile:

                # get note contenant and try to match it
                content = cfile.read()

                if re.search(regex, content, re.IGNORECASE) is not None:
                    displayNote(path, linesDisplayedWhenList)
                    i += 1

        # nothing found
        if i < 1:
            print("Nothing found: " + join(unkArgs, ", "))

        exitProgram()

    # Error while parsing arguments
    print("Syntax error, please read help below: ")
    parser.print_help()
    exitProgram(1, "")
