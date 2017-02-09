# Memo sur le script bash

Conditions et tests:

	Pour les tests toujours préferer [[ à [
	

	# tester si une variable est déclarée
	if [[ -z "$HEYHEY" ]] ; then
		echo "$HEYHEY exist"
	fi

	# Tester si une commande existe ou quitter
	command -v foo >/dev/null 2>&1 || {     echo >&2 "I require foo but it's not installed.  Aborting."; exit 1;}

	# Tester si une commande existe
	if hash gdate 2>/dev/null; then
		# gdate existe
		gdate "$@"
	else
		# gdate n'existe pas
		date "$@"
	fi

	# Tester si un paquet est présent et l'installer au besoin
	dpkg -s package &> /dev/null

	if [ $? -ne 0 ]; then
			echo "Installation"
			apt-get install package
	fi
	
	# tester si un fichier est executable
	if [[ -x "$file" ]]
	then
		echo "File '$file' is executable"
	else
		echo "File '$file' is not executable or found"
	fi

	# expression ternaire
	MESSAGE=$([ -z "$@" ] && echo "Alerte !" || echo $@);
	
	# tester si root
	if [ "$(whoami)" != 'root' ]; then
			echo "You have no permission to run $0 as non-root user."
			exit 1;
	fi

	# tester un fichier 
	if [ -e "$FILE" ]; then
		echo "$FILE exist"
	fi

	# tester un répertoire
	if [ -d "$FILE" ]; then
		echo "$FILE exist"
	fi
	
	# Comparer des entiers. Attention aux espaces.
	if [ "$a" -eq "$b" ]; then

	fi

	-eq: =
	-ne: !=
	-gt: >
	-ge: >=
	-lt: >
	-le: >=

	# Comparer des chaines
	if [ "$a" = "$b" ]; then

	fi
	if [ "$a" != "$b" ]; then

	fi

	# vérifier si une chaine est vide,
	if [ -z "$VAR" ]; then
			echo "$VAR is empty"
			exit 1
	fi

	# inverser une condition: !
	if ! [ -z "$VAR" ]; then

	fi


	VAR="hello"
	if [ -n "$VAR" ]; then
		echo "VAR is not empty"
	fi
	
	# Afficher une date
	echo `date`;
	cat << EndOfMessage
	This is line 1.
	This is line 2.
	Line 3.
	EndOfMessage
	# Effectuer des calculs
	echo $((1+1));

	# incrémenter une variable
	export VAR=1
	echo $((++VAR))
	
	# Test. Faux retourne 0 / Vrai retourne 1
	export VAR=1
	echo $((VAR==2))



Commandes diverses:

	# Substitution de commande (deux syntaxes similaires)
	export DATE=`date`;
	export DATE=$(date);

	# chiffre aleatoire entre 2 et 6
	RANDOMNBR=`shuf -i 2-6 -n 1`
	sleep $RANDOMNBR

	# date formatee
	date +'%Y-%m-%d_%H-%M-%S'

	# créer tous les repertoire du chemin
	mkdir -p /path/to/dir
	
	# multi ligne
	cat << EndOfMessage
	This is line 1.
	This is line 2.
	Line 3.
	EndOfMessage

	# obtenir le chemin du script, ne fonctionne pas si l'appel se fait a partir d'un lien symbolique
	DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
	
	# Changer les droits et executer en une commande, sans risque d'échec grâce à "sync"
	cd /opt/dependencies && chmod +x get-dependencies.sh && sync && ./get-dependencies.sh
	
	# Activer / desactiver le mode debuggage
	set -x
	set +x
	
Entrées et sorties:

	# Ecrire en bleu
	echo -e "\e[34mHello\e[0m World"

	# lire l'entrée utilisateur dans une variable
	read -e ONE_LINE

	# récupérer l'entrée standard
	STDIN=$(cat)

	# équivalent à 
	STDIN=$(cat /dev/stdin)

	# récupérer l'entrée standard (pipe)
	if [ -t 0 ]; then
		echo "No stdin"
	else
		STDIN=$(cat)
		echo "Stdin: $STDIN"
	fi
	
	# demander une confirmation
	if [[ $RESPONSE =~ ^(yes|y| ) ]]; then
		echo "Yes"
        break
	elif [[ $RESPONSE =~ ^(quit|q) ]]; then
		echo "Quit"
	else
		echo "No"
	fi


Variables : 

	VAR="val" # Pas d'espaces !!!

	# Variables spéciales:

	echo $# # contient le nombre de paramètres ;
	echo $0 # contient le nom du script exécuté (ici ./variables.sh) ;
	echo $1 # contient le premier paramètre ;
	echo $2 # contient le second paramètre ;
	echo # + commande shift


Fonctions :

	# Attention à l'espace après function 

	# fonction, paramètres et retours
	function dosomething {
		OUTPUT="That's done: $@ $1"
		echo $OUTPUT
	}

	# executer la fonction avec argument, et récuperer le retour
	RESULT=$(dosomething "do something today")
	
	# ou executer tout simplement
	dosomething


Boucles : 

	# boucles
	while [ $i -lt 4 ]; do
		echo $i
		i=$[$i+1]
	done

	while true; do
		eject
		espeak Yooooooloooooooo
		sleep 1s;
	done


