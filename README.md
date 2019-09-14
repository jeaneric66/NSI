<h1>Infos pour NSI</h1>


<hr>

Installer un système d'exploitation linux sur une clé USB !
<hr>

Le matériel : deux clés USB dont une si possible USB 3 (au moins 32Go) sur laquelle on va installer un système d'exploitation linux, La seconde clé sert dépôt intermédaire (8Go à 16 Go) suffisent et deux ordinateurs,un en état de marche avec OS windows et celui sur lequel on veut faire tourner l'OS linux.

<hr>

1. Installer sur la machine bien portante en OS windows, installer le logiciel Rufus : [Rufus](https://rufus.ie/fr_FR.html)

2. Télécharger l'image .iso d'un système d'exploitation linux tel que linux Debian ou Linux xubuntu.
[xubuntu](https://xubuntu.org/download/) ou  [Debian](https://www.debian.org/CD/live/)

Vous avez ici le choix entre une version 32bits ou 64bits ??? Internet est votre ami par exemple [](https://www.astuces-aide-informatique.info/2738/windows-32-bits-ou-64-bits)

Bref on télécharge un .iso et c'est assez lourd.

3. Une fois intallé le logiciel Rufus et le .iso (bien savoir dans quel répertoire est ce .iso, en général le dossier téléchargement), on lance le logiciel Rufus après avoir mis la clé USB qui sert de dépôt intermédiaie dans un port USB de l'ordinateur.

Suivre alors la doc de Rufus : installer sur la clé (en, général le dossier D: ou E:) mais surtout pas C: !!!!!!!, l'iso téléchargé. Cela prend quelques minutes. Après cette première manipulation vous avez un système d'exploitation utilisable sur cette première clé.

4. Sur la machine "malade", on insère la clé USB (qui a le système Linux) et on démarre l'ordinateur touche F2 enfoncée (cela peut être F?? suivant l'ordinauteur...) le but est d'accéder au BIOS. Une fois dans le BIOS le but est de changer l'ordre de démarrage des périphériques, et de mettre en premier la clé USB puis le disque dur habituel. On enregistre cet ordre et avant de quitter le BIOS :

5. On insère la seconde clé USB (celle sur laquelle on veut installer le système Linux), et on continue la procédure de démarrage.

6. Si tout est OK le système Linux démarre et vous propose soit de l'essayer soit de l'installer ! Il faut choisir de l'installer sur la seconde clé USB !!!! Attention si vous choisissez votre disque dur de machine Windows, il sera écrasé définitivement (ce qui n'est pas grave si il ne fonctionnait plus, mais c'est nettement plus grave si il est toujours opérationnel et que l'ordinateur sert à toute votre famille !!! Là faut faire vraiment gaffe, surtout si votre ordinateur contient de nombreuses données !!!!!)

En clair on installe le système Linux sur la clé USB 3 à partir de la clé qui sert de dépôt.

7. Bon là il n'y a plus qu'à répondre aux questions liés à l'installation, cette dernière est plus ou moins longue suivant la rapidité des ports USB et des clés choisies !

8. Un fois l'installation terminée, il suffit alors d'enlever la clé qui a servie de dépôt intermédiaire et de démarrer l'ordinateur sur la clé USB 3 sur laquelle est installé l'OS Linux choisi de manière pérenne !

<hr>
