# Installer et utiliser Apache Tomcat

# Installation et démarrrage

	$ cd /opt
	$ wget http://apache.mediamirrors.org/tomcat/tomcat-9/v9.0.0.M13/bin/apache-tomcat-9.0.0.M13.zip  
	$ unzip apache-tomcat...zip
	$ cd apache-tomcat.../bin
	$ chmod +x *.sh
	$ ./startup.sh

	$ ./catalina.sh stop
	$ ./catalina.sh start

A l'écoute sur le port 8080 par défaut.

# Déploiement

Les déploiements se font sours forme d'archives ou dézippés dans le dossiers 'webapps'.

# Administration

Interface disponible à l'adresse http://127.0.0.1:8080.
Pour ajouter un utilisateur:

	$ vim conf/tomcat-users.xml

	Exemple d'utilisateur autorisé à utiliser l'application de management (manager-gui):
	
	<user username="tomcat" password="tomcat" roles="manager-gui"/>

# Erreurs courantes

	L'application à été déployée mais le contexte n'a pas pu être démarré ...

	$ mvn tomcat7:redeploy

	Ou:

	$ mvn clean
	$ mvn tomcat7:undeploy
	$ mvn tomcat7:deploy

	

