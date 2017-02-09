# Installer et utiliser OpenVPN

# Installer 

Sur Ubuntu 16.04 64 bits

        $ wget http://swupdate.openvpn.org/as/openvpn-as-2.1.2-Ubuntu16.amd_64.deb
        $ sudo dpkg -i openvpn-as-2.1.2-Ubuntu16.amd_64.deb

Definir un mot de passe par défaut à l'utilisateur 'openvpn':

        $ sudo passwd openvpn
       
Ensuite visiter cnfigurer le serveur avec un navigateur web à l'adresse:

        https://137.74.161.106:943/admin # pour la configuration

Définir éventuellement d'autres utilisateurs.

# Utiliser

Visiter la page suivante puis se connecter:

        https://137.74.161.106:943/      # pour la connexion
        
Sur un poste client Linux:

		# Installer le client
		$ sudo apt-get install openvpn
		
		# Télécharger la configuration à l'aide d'un navigateur web. Nom du fichier: 'client.ovpn'
		# Puis démarrer le service:
		$ openvpn --config client.ovpn
		
Pour utiliser OpenVPN sur 443 installer sslh puis modifier la configuration .ovpn comme suit:

		-- /!\ ne fonctionne qu'avec TCP, pas avec UDP
		remote vps303506.ovh.net 443 tcp


		
