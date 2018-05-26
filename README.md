# Python experiments

Various uninteresting experiments and examples on Python. Some are not documented here.

My favorite everyday scripts are in repo "linux-utils" !

## ncurses/let-it-snow.py
Let it snow !

## backup.py
Small backup utility. Directories are hard coded in script.

Usage:

```
usage: backup.py [-h] [-w] [-n] [-d] [-l] [-e]

Sauvegarde de dossiers sur le disque dur tradtionnel. Dossiers: ...

optional arguments:
  -h, --help     show this help message and exit
  -w, --week     effectuer une sauvegarde hebdomadaire si necessaire
  -n, --now      effectuer une sauvegarde immédiatement
  -d, --display  afficher les sauvegardes disponibles
  -l, --log      afficher les dernières lignes du journal
  -e, --edit     editer ce script de sauvegarde
```

## leet.py
Transform string in a badass way :)

Usage:

```
optional arguments:
  -h, --help  show this help message and exit
```

## chainedCommands.py
Utility usefull to chain GNU/Linux commands.

Example:
```
C("log.txt").c("mkdir dir1").c("cd dir1").c("...")
```

## node.py
Utility used to draw trees.

Example:

```
tree1 = Node("*",
            Node("-",
                 Node("u"), Node("^",
                                 Node("+",
                                    Node("x"), Node("*",
                                                    Node("y"), Node("log",
                                                                    Node("-",
                                                                         Node("z"), Node("5"))))),
                                 Node("3"))),
             Node("2"))

TreeWindow(tree1).show()

# In a command prompt:
$ ./node.py
```

![Screenshot](screenshots/2016-03-31-00-23-55.png)
