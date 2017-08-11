# coding: utf-8
import re

"""
Exemple :
Avant :
  1 - 9wm
      2 - a2ps
      3 - abiword
      4 - access
      5 - aconnect
      6 - alevtd
      7 - alien

Après :
9wm
a2ps
abiword
access
aconnect
alevtd
alien
"""

for i in xrange(1,10):
	with open("../bots/prog_assist/sets/man"+str(i)+'.txt', 'r+') as source:
		data=source.read()
		data = re.sub(r'(?m)^\s*\d+ - ([\w\-.]+)',r'\1',data)
		source.seek(0, 0)
		source.truncate()
		source.write(data)