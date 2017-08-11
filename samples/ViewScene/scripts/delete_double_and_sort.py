# coding: utf-8
import re
"""
Delete double between all website and sort alphabetically
(case insensitive)
"""
for i in xrange(1,10):
	with open("../bots/prog_assist/sets/man"+str(i)+'.txt', 'r+') as source:
		data=source.readlines()
		new=[]
		s = set([d.lower() for d in data])
		while(s):
			new.append(s.pop())
		source.seek(0, 0)
		source.truncate()
		new.sort()
		source.writelines(new)