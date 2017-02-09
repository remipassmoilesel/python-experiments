# Installer Flash sur Firefox

Télécharger Flash player.

Puis le décompresser et l'installer:

	$ cd Downloads
	$ tar -xvf install-flash.####.tar
	$ sudo cp libflashplayer.so /usr/lib/mozilla/plugins

Ensuite redémarrer le navigateur et vérifier le fonctionnnement du plugin sur:

	about:plugins
