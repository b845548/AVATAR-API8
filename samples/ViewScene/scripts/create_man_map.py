# coding: utf-8
import re

"""
fusionne les set des différents man et créer un map donnant la catégorie du man
"""
with open("../bots/prog_assist/sets/man.txt", 'w') as dest, open("../bots/prog_assist/maps/man.txt", 'w') as final:
	for i in xrange(1,10):
		with open("../bots/prog_assist/sets/man"+str(i)+'.txt', 'r') as source:
			data=source.readlines()
			if data[-1][-1] !='\n':
				data[-1] += '\n'
			dest.writelines(data)
			final.writelines([d[:-1]+':'+str(i)+'\n' for d in data])