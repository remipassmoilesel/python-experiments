# Postgres: installation rapide et memo

/!\ Attention, lors de la création de base de donnée, si le nom est spécifié entre double quote il faudra 
spécifier systèmatiquement les double quote et le nom deviendra sensible à la casse

Installer:

    $ sudo apt-get update
    $ sudo apt-get install postgresql pgadmin3

Démarrer:

    $ sudo service postgresql start

Executer une commande directement:

    $ sudo -u postgres psql -c "CREATE DATABASE somename"

Ouvrir un shell en tant que postgres

    $ sudo -i -u postgres

Créer un super user au nom de l'utilisateur courant, sans mot de passe:
    
    $ createuser -s -w remipassmoilesel

Ou en mode interactif:
    
    $ createuser --interactive

Retour au shell classique
    
    $ exit

Créer une bdd au nom de l'user unix
    
    $ createdb remipassmoilesel

Ouvrir une bdd

    $ psql remipassmoilesel

Importer à partir d'un dump
    
    $ psql databasename < data_base_dump

Commandes psql
    
    \q  : quitter
    \h  : aide
    \d+ : nomtable
    \l  : décrire une table 

Pour supprimer une base de donnée et un utilisateur
    
    dropdb bdname
    dropuser username

Modifier le mot de passe d'un utilisateur:

    $ sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres';"

