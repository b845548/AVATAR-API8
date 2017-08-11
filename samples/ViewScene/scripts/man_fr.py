# coding: utf-8
from __future__ import unicode_literals
import urllib2, os, sys, re
from bs4 import BeautifulSoup

if len(sys.argv) < 3:
		print "Error in file use, 'python man_fr.py [man_entry] [man_category_number]'"
		quit()

def clean_spaces(matchobject):
	clean = re.sub(r'\s{2,}', ' ', matchobject.group(1))
	return re.sub(r'^\s*', '\n\t', clean)

command = sys.argv[1].lower()
try: # http://www.linux-france.org/article/man-fr/
	page =  BeautifulSoup(urllib2.urlopen('http://www.linux-france.org/article/man-fr/man'+sys.argv[2]+'/'+command+'-'+sys.argv[2]+'.html'), "html.parser")
	text = page.body.get_text()
	text = re.sub(r"(?s)^.*?(?=NOM)",'',text)
	text = re.sub(r"""(?xu)\s+?\n .+? [ \t]+
		\d{1,2}\ [A-Z][a-zéû]+\ \d{4} #date
		[ \t]+ \d+\s+
		(?:.+\n)?""",'',text)

except urllib2.HTTPError:
	try: # http://www.man-linux-magique.net/
		page =  BeautifulSoup(urllib2.urlopen('http://www.man-linux-magique.net/man'+sys.argv[2]+'/'+command+'.html'), "html.parser")
		text = page.find(id="texte-man").get_text()
		text = re.sub(r"\n+$",'',text)
	
	except urllib2.HTTPError:
		try: # http://jp.barralis.com/linux-man/
			# étape intermédiaire nécessaire car ce site ne déclenche pas HTTPError 404
			request = urllib2.urlopen('http://jp.barralis.com/linux-man/man'+sys.argv[2]+'/'+command+'.'+sys.argv[2]+'.php')
			url = request.geturl()
			if url == 'http://jp.barralis.com/linux-man/404man.php':
				raise urllib2.HTTPError(url, 404, "Ce man n'existe pas...", request.info(), None)
			page =  BeautifulSoup(request, "html.parser")
			text = page.body.get_text()
			text = re.sub(r"""(?xs)^.*?(?=NOM) |
				\n+<!--.* | #commentaires et scripts de fin
				\xa0""",'',text) #&nbsp;

			# rectification de l'indentation
			text = re.sub(r"""(?mux)^((?:[^A-ZŒÆÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇ\n]+? |
				[A-ZŒÆÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇ][^A-ZŒÆÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇ\n]+?)
				.*)$""",r'\t\1',text)

			# rectification de l'indentation des options
			text = re.sub(r"(?m)^(\t-.+\n)\s*?\n(\t[^\-].*$)",r'\1\t\2',text)

			# regrouper la description
			text = re.sub(r"(?s)(?<=DESCRIPTION\n)(.+?)(?=\n\n[A-ZŒÆÀÂÄÉÈÊËÏÎÔÖÙÛÜŸÇ])", clean_spaces, text)
			
			# regrouper synopsis/syntaxe
			m = re.search(r'(?u)NOM\s*(\w+)', text)
			name = m.group(1) if m is not None else command
			text = re.sub(r"""(?x)(\t\[\n
				(?: [^\[]*? (?:\[ [^\[]*? \])*)*?
				\])""", clean_spaces, text)
			text = re.sub(r"]\s+\[", r'] [', text)
			text = re.sub(r"(?x)("+name+""")
				\s+?\n\[""", r'\1 [', text)
		
		except urllib2.HTTPError:
			print u"Défaillance du système, je n'ai pas pu consulter le manuel".encode('utf-8')
			quit()

except urllib2.URLError:
	print u"Je suis actuellement trop déprimé par l'absence d'une connexion à internet pour te répondre.".encode('utf-8')
	quit()

print (command+'('+sys.argv[2]+')\n\n'+text).encode('utf-8')