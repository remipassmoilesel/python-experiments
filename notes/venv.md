# Virtual-Env

Voir: http://sametmax.com/les-environnement-virtuels-python-virtualenv-et-virtualenvwrapper/

Installation:

    $ sudo pip3 install virtualenv 

Créaton:

    $ virtualenv --no-site-package .venv 

Activation:

    $ source .venv/bn/activate
    $ pip install docker-py
    
Version différente de python:
    
    $ virtualenv mon_env -p /usr/bin/python2.6