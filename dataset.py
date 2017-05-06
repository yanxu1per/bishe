#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs,chardet
import pdb
import re

f=codecs.open('pro','r','utf-8')
f2=codecs.open('haveweight.txt','r','utf-8')
fo=open('dataset2','w')
lines=f.readlines()
lines2=f2.readlines()
for line in lines:
	line=line.strip()[0:-1]
	try:
		target=re.findall('target\:"(.*?)"',line)[0]
	except:
		pdb.set_trace()
	if target=='车'.decode('utf-8'):
		
		
		#fo.write('{} {}\n'.format(target.encode('utf-8'),source.encode('utf-8')))
		continue
	source=re.findall('source\: "(.*?)"',line)[0]
	#pdb.set_trace()
	
	for ll in lines2:
		if ll.strip().split('	')[0]==source and int(ll.strip().split('	')[3])>=30:
			fo.write('{} {} {} {}\n'.format(target.encode('utf-8'),source.encode('utf-8'),ll.strip().split('	')[1].encode('utf-8'),ll.strip().split('	')[2].encode('utf-8')))
			#pdb.set_trace()
			


	
