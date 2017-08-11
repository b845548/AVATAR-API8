# coding: utf-8
import re

"""
Exemple :
Avant :
apropos
      Rechercher  une chaîne de caractère dans la base de
      données whatis.

arch   Afficher l'architecture de la machine.

at, batch, atq, atrm
      Mémoriser,  examiner  ou  supprimer  des   jobs   à
      exécuter ultérieurement.

basename
      Eliminer  le  chemin d'accès et le suffixe d'un nom
      de fichier.

Après :
apropos
arch
at
batch
atq
atrm
basename
"""

for i in xrange(1,10):
	with open("../bots/prog_assist/sets/man"+str(i)+'.txt', 'r+') as source:
		data=source.readlines()
		new=[]
		for line in data:
			match=re.search(r'^([\w\-.]+(?:, [\w\-.]+)*)', line)
			if match is not None:
				command = match.group(1)
				commands = re.split(', ', command)
				for c in commands:
					new.append(c+'\n')
		source.seek(0, 0)
		source.truncate()
		source.writelines(new)