# coding: utf-8
from __future__ import unicode_literals
import wikipedia, requests

wikipedia.set_lang("fr")
while True:
	try:
		print wikipedia.summary(wikipedia.random()).encode('utf-8')
		break

	except wikipedia.exceptions.DisambiguationError:
		pass
	except wikipedia.exceptions.PageError:
		pass
	except requests.exceptions.ConnectionError:
		print u"Je suis actuellement trop déprimé par l'absence d'une connexion à internet pour te répondre.".encode('utf-8')
		break