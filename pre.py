#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs,chardet
import pdb
import re
from random import choice

f=codecs.open('dataset2','r','utf-8')
f2=codecs.open('att7','r','utf-8')
fo=open('result','w')

mol={}
lines=f.readlines()
for line in lines:
	sp=line.split()
	if not mol.get(sp[0]):
		mol[sp[0]]={}
	if not mol[sp[0]].get(sp[1]):
		mol[sp[0]][sp[1]]={}
	if not mol[sp[0]][sp[1]].get(sp[3]):
		mol[sp[0]][sp[1]][sp[3]]=[]
	mol[sp[0]][sp[1]][sp[3]].append(sp[2])

de0=['说起 这款车']
de1=['还算','只能说','勉强谈得上','偏','略显']
de2=['的确','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉']
de3=['非常','很','特别','真是','超级','给人非常 的感觉','过于','太过']
de4=['方面']
blank=['其他的呢']
d1=set(['偏','略显','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','很','特别','真是','只能说'])
d2=set(['勉强谈得上','的确','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','非常','很','特别','真是','超级','给人非常 的感觉'])
d3=set(['非常','很','特别','真是','超级','给人非常 的感觉','过于','太过','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','比较','勉强谈得上'])
total=de1+de2+de3


for fangmian in mol.keys():
	
	for att in mol[fangmian]:
		try:
			for item in mol[fangmian][att]['-1']:
				fo.write(att.encode('utf-8')+' '+item.encode('utf-8')+'\t')
				for d in total:
					if d in d1:
						fo.write(str(1)+'\t')
					else:
						fo.write(str(0)+'\t')
				fo.write('\n')
		except:
			pass
		try:
			for item in mol[fangmian][att]['0']:
				fo.write(att.encode('utf-8')+' '+item.encode('utf-8')+'\t')
				for d in total:
					if d in d2:
						fo.write(str(1)+'\t')
					else:
						fo.write(str(0)+'\t')
				fo.write('\n')
		except:
			pass
		for item in mol[fangmian][att]['1']:
			fo.write(att.encode('utf-8')+' '+item.encode('utf-8')+'\t')
			for d in total:
				if d in d3:
					fo.write(str(1)+'\t')
				else:
					fo.write(str(0)+'\t')
			fo.write('\n')


		