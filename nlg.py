#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs,chardet
import pdb
import re
from random import choice,shuffle

de0=['说起 这款车']
de1=['还算','只能说','勉强谈得上','偏','略显']
de2=['的确','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉']
de3=['非常','很','特别','真是','超级','给人非常 的感觉','过于','太过']

d1=set(['偏','略显','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','很','特别','真是','只能说'])
d2=set(['勉强谈得上','的确','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','非常','很','特别','真是','超级','给人非常 的感觉'])
d3=set(['非常','很','特别','真是','超级','给人非常 的感觉','过于','太过','给人一种 的感觉','让我觉得','','有些','感觉','勉强谈得上','的确','比较'])
de4=['方面']
blank=['其他的呢','再有呢','和我之前那一辆车比起来','还算不错 毕竟咱也不是专业车手','个人觉得还算满意','买了之后没有什么太大的遗憾','还是家人觉得好就好','我也不奢求太多']

def formsen(att,d,adj):
	
	if len(d.split())>1:
		return att.encode('utf-8')+adj.encode('utf-8').join(d.split())
	elif d=='':
		return att.encode('utf-8')+adj.encode('utf-8')
	return att.encode('utf-8')+d+adj.encode('utf-8')

def encode(code,fangmian,att):
	global de1,de2,de3,d1,d2,d3,mol
	if code=='000':
		adj=choice(mol[fangmian][att]['0'])
		d=choice(list(set(de2)|d3))
	elif code=='100':
		adj=choice(mol[fangmian][att]['1'])
		d=choice(list(set(de3)|d3))
	elif code=='110':
		adj=choice(mol[fangmian][att]['-1'])
		d=choice(list(set(de0)|d3))
	elif code=='111':
		adj=choice(mol[fangmian][att]['0'])
		d=choice(list(set(de2)|d2))
	elif code=='010':
		adj=choice(mol[fangmian][att]['1'])
		d=choice(list(set(de3)|d2))
	elif code=='011':
		adj=choice(mol[fangmian][att]['-1'])
		d=choice(list(set(de1)|d2))
	elif code=='001':
		adj=choice(mol[fangmian][att]['1'])
		d=choice(list(set(de3)|d1))
	elif code=='101':
		adj=choice(mol[fangmian][att]['-1'])
		d=choice(list(set(de1)|d1))

	return formsen(att,d,adj)
chexin=raw_input()
code='10101101001010101010'
length=len(code)
if length%3==1:
	code=code+'0'
	length+=1
if length%3==2:
	code+='00'
	length+=2
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
	#pdb.set_trace()


text=''
text+=chexin.join(de0[0].split())+' '
#pdb.set_trace()
count=0
eos=0

for fangmian in mol.keys():
	#flag=0
	text+=fangmian.encode('utf-8')+de4[0]+' '
	for att in mol[fangmian]:
		if count+3>=length and eos==0:
			eos=1
			text+=choice(blank)+' '
			break
		if eos==0:
			co=code[count:count+3]
			count+=3
			sen=encode(co,fangmian,att)
			text+=sen+' '
		else:
			bit=[0,1]
			co=str(choice(bit))+str(choice(bit))+str(choice(bit))
			sen=encode(co,fangmian,att)
			text+=sen+' '

print text


