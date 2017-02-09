# Créer une clef USB à partir d'une machine virtuelle

Création de la VM:
	
	....

Conversion au format raw:

	$ VBoxManage internalcommands converttoraw lubuntu.vdi lubuntu.raw

Changer la taille d'un fichier vdi (taille en Mo):

	$  VBoxManage modifyhd ubuntu32-vs-wild.vdi --resize 16000 

Ecriture (attention au sync):

	$ sudo dd if=lubuntu.iso of=/dev/sdc bs=4M && sync

/!\ Les clefs ne bootent pas encore partout !
