#!/usr/bin/python2.7
# encoding: utf-8

import argparse
import datetime
import os
import re
import shutil
import subprocess
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
encryptedNoteExtension = "gpg"

# template path
noteTemplateName = ".template.md"
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


def displayNote(notePath, lineMax=None, regex=None):
    """
    Display a note, without first blank lines
    """
    print(bcolors.OKGREEN + "@ Number: " + str(
        listNotePaths().index(notePath)) + bcolors.ENDC)
    print("@ Name: " + notePath.split(os.sep)[-1])
    print("@ Path: " + notePath)
    print("")

    i = 0
    firstPrinted = False
    for line in getLinesFromNote(notePath):

        # avoid printing first empty lines
        if firstPrinted is False and re.search("[a-z0-9]+", line, re.IGNORECASE) is None:
            continue
        else:
            firstPrinted = True

        # first line; print in color. [0:-1] print without end of line
        if i == 0:
            print(bcolors.OKBLUE + bcolors.UNDERLINE + line[0:-1] + bcolors.ENDC)
            print("")
            i +=1

        # otherwise print normally, but without end of line
        else:
            if regex == None:
                print(line[0:-1])
                i += 1
            # if regex is provided, show only matching lines
            else:
                match = re.search(regex, line, re.IGNORECASE)
                if match != None:
                    line = re.sub(regex, bcolors.WARNING + match.group(1) + bcolors.ENDC, line, re.IGNORECASE)
                    print(line[0:-1])
                    i += 1

        if lineMax != None and i > lineMax:
            break

    if i == 0:
        print " ** Note is empty ** "

    print("")


def resolveNoteName(data, includeEncrypted = False):
    """
    Try to resolve a note name regardless it is a note name, partial name or number.
    Return None if nothing is found
    """
    # arg is a full path
    if os.path.isfile(data) == True:
        return data;

    # arg is a note number
    if re.search("^[0-9]*$", data):
        notes = listNotePaths(includeEncrypted)
        if int(data) < len(notes):
            return notes[int(data)]

    # arg is a relative path or a partial name
    if len(data.split(os.sep)) < 2:

        # relative path: return absolute path
        notePath = os.path.join(notesRepPath, data)
        if os.path.isfile(notePath):
            return notePath

        # partial name: search
        for path in listNotePaths(includeEncrypted):
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


def listNotePaths(includeEncrypted = False):
    """
    Return an ordered list of note paths
    """

    # list files from directory
    output = []
    dirList = os.listdir(notesRepPath)

    # remove uneeded files
    for fname in dirList:
        if fname != "." and fname != ".." and fname != noteTemplateName:
            if (includeEncrypted and fname.endswith(encryptedNoteExtension)) \
                    or fname.endswith(noteExtension):
                output.append(os.path.join(notesRepPath, fname))

    output.sort()

    # return result
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
            print("Note repository was created here: " + notesRepPath)
        except:
            exitProgram(1, "Unable to create note repository: " + notesRepPath)

    # check note template
    if os.path.isfile(noteTemplatePath) == False:
        try:
            open(noteTemplatePath, 'a').close()
        except:
            exitProgram(1,
                        "Unable to create note template here: " + noteTemplatePath)


def encryptGpg(noteName):
    """
    Encrypt with GPG
    """
    code = subprocess.call("gpg --yes --armor --output " + clearToEncryptedNoteName(noteName)
                           + " --symmetric " + noteName + " && sync", shell=True)

    # then destroy clear file
    code += subprocess.call("shred -u " + noteName + " && sync", shell=True)

    return code


def decryptGpg(noteName):
    """
    Decrypt with GPG
    """
    return subprocess.call("gpg --yes --decrypt --output " +
                           encryptedToClearNoteName(noteName) + " " + noteName + " && sync", shell=True)

def clearToEncryptedNoteName(noteName):
    return noteName + "." + encryptedNoteExtension

def encryptedToClearNoteName(noteName):
    return noteName[:-4]

if __name__ == "__main__":

    # check repo
    checkNoteRepository()

    # parse arguments
    parser = argparse.ArgumentParser(description=PGRM_DESC)

    parser.add_argument("-k", "--encrypt",
                        action="store_true",
                        help="encrypt with gpg (symetric) after edit")

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
            noteName = createNewNote(unkArgs[0])
        else:
            noteName = createNewNote()

        # create note
        print("This note have been created: " + noteName)

        # then edit it
        editNote(noteName, knownArgs.graphicaleditor)

        # if necessary, encrypt it
        if knownArgs.encrypt == True:
            code = encryptGpg(noteName)
            if code != 0:
                exitProgram(1, "/!\ Warning: Error while encrypting note " + noteName)

        exitProgram()

    # edit existing note
    if knownArgs.editnote:

        # check if exist
        if len(unkArgs) != 1:
            exitProgram(1, "You must specify a name, a partial name or a number.")

        # get path of note
        notePath = resolveNoteName(unkArgs[0], knownArgs.encrypt)

        # not found
        if notePath == None:
            exitProgram(1, "Unable to found note: " + unkArgs[0])

        # decrypt it if needed
        if knownArgs.encrypt == True:
            code = decryptGpg(notePath)
            notePath = encryptedToClearNoteName(notePath)
            if code != 0:
                exitProgram(1, "/!\ Unable to decrypt note: " + notePath)

        # edit it
        editNote(notePath, knownArgs.graphicaleditor)

        # encrypt if needed
        if knownArgs.encrypt == True:
            code = encryptGpg(notePath)
            if code != 0:
                exitProgram(1, "/!\ Warning: Error while encrypting note " + notePath)

        exitProgram()

    # edit template
    if knownArgs.edittemplate:
        editNote(noteTemplatePath, knownArgs.graphical_editor)

        exitProgram()

    # list existing notes
    if knownArgs.list:

        notePaths = listNotePaths()
        if len(notePaths) < 1:
            exitProgram(0, "No notes available in: " + notesRepPath)

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

        displayNote(notePath)

        exitProgram()

    # display all
    if knownArgs.displayall:

        print("Notes from directory: " + notesRepPath)
        print("")

        for path in listNotePaths():
            displayNote(path)

        exitProgram()

    # search in notes
    if knownArgs.search:

        # check keywords
        if len(unkArgs) < 1:
            exitProgram(1, "You must specify keywords.")

        print("Notes from directory: " + notesRepPath)
        print("")

        # create a search regex
        regexa = []
        for w in unkArgs:
            regexa.append(re.sub("[^a-z]", ".?", w, re.IGNORECASE))

        regex = "(" + join(regexa, "|") + ")+"

        log("searching notes: regex: " + regex)

        # iterate notes and search keywords
        i = 0
        for path in listNotePaths():

            with open(path, 'r') as cfile:

                # get note content and try to match it
                content = cfile.read()

                searchResult = re.findall(regex, content, re.IGNORECASE)
                if searchResult:
                    displayNote(path, linesDisplayedWhenList, regex)
                    i += 1

        # nothing found
        if i < 1:
            print("Nothing found: " + join(unkArgs, ", "))

        exitProgram()

    # Error while parsing arguments
    print("Syntax error, please read help below: ")
    parser.print_help()
    exitProgram(1, "")
