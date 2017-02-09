# Alpine Linux

Parfaite pour des conteneurs ?

Pour avoir accès aux scripts de démarrage installer le package openrc:
    
    $ apk add openrc

## Gestionnaire de paquets

Mise à jour de l'index
    
    $ apk update

Installer un paquet

    $ apk add package

Mettre à jour tout le système

    $ apk update
    $ apk upgrade

Mettre à jour seulement quelques paquets

    $ apk add --upgrade busybox 

Lister tous les paquets

    $ apk search -v

Rechercher

    $ apk search -v 'acf*'

Montrer toutes les infos sur un paquet
    
    $ apk info -a zlib

# Lister les paquets installés

    $ apk info

Source: https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Update_the_Package_list



