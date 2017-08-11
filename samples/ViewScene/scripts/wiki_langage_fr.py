# coding: utf-8
from __future__ import unicode_literals
import os, sys, wikipedia, requests

if len(sys.argv) < 2:
		print "Error in file use, 'python langage_descr_fr.py [language_name]'"
		quit()

# J'avais commencé à écrire le parseu wikipédia à la main en utilisant l'API wikimédia, puis j'ai découvert la lib python wikipedia
# url = "https://fr.wikipedia.org/w/api.php"
# params = {'action': 'query', 'titles':' '.join(sys.argv[1:]), 'prop':'extracts', 'exsectionformat':'plain', 'format':'json'}
# r = requests.get(url, params=params)
# if r.status_code == 200:
# 	r.encoding = 'utf-8'
# 	print r.json()['query']['pages']

langage = ' '.join(sys.argv[1:]).upper()
if langage == "C#":
	langage = "C sharp"

ambiguity = (u"Moi et mon ami Wikipédia somme en désaccord sur la définition de "+langage+".\nJe ne peux donc pas te l'expliquer pour l'instant.").encode('utf-8')
not_found = u"Ce langage est désué. Tellement désué qu'il n'y a même pas d'article wikipédia dessus.\nApprennez-en un autre. Mais genre vraiment.".encode('utf-8')

wikipedia.set_lang("fr")

try:
	result = wikipedia.page(langage)
	# nécessaire à cause de l'autosuggest qui peut nous faire passer de cesil à César,
	# mais dont on a besoin pour passer de abap à ABAP
	if result.title.upper() != langage:
		raise wikipedia.exceptions.PageError(langage)
	print result.summary.encode('utf-8')


except wikipedia.exceptions.DisambiguationError as e:
	# possibilities = wikipedia.search(langage)
	# for p in possibilities:
	# 	if "langage" in p:
	# 		langage=p
	# 		break
	# else:
	# 	print ambiguity
	# 	quit()
	try:
		result = wikipedia.page(langage+" (langage)")

		if result.title.upper() != langage+" (LANGAGE)":
			raise wikipedia.exceptions.PageError(langage)

		print result.summary.encode('utf-8')

	except wikipedia.exceptions.DisambiguationError as e:
		print ambiguity

	except wikipedia.exceptions.PageError as e:
		print not_found

except wikipedia.exceptions.PageError as e:
	print not_found

except requests.exceptions.ConnectionError:
	print u"Je suis actuellement trop déprimé par l'absence d'une connexion à internet pour te répondre.".encode('utf-8')