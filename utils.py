#!/usr/bin/python
# -*- coding: UTF-8 -*-

from config import config
from random import choice,shuffle
import re

conf=config()
#pdb.set_trace()
de0=conf.de0
de1=conf.de1
de2=conf.de2
de3=conf.de3

d1=conf.d1
d2=conf.d2
d3=conf.d3
de4=conf.de4
blank=conf.blank
mol=conf.formmol()
imol=conf.formimol()
d=d1 | d2 | d3

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
		d=choice(list(set(de1)&d2))
	elif code=='100':
		adj=choice(mol[fangmian][att]['1'])
		d=choice(list(set(de1)&d3))
	elif code=='110':
		adj=choice(mol[fangmian][att]['-1'])
		d=choice(list(set(de1)&d1))
	elif code=='111':
		adj=choice(mol[fangmian][att]['0'])
		d=choice(list(set(de2)&d2))
	elif code=='010':
		adj=choice(mol[fangmian][att]['1'])
		d=choice(list(set(de2)&d3))
	elif code=='011':
		adj=choice(mol[fangmian][att]['-1'])
		d=choice(list(set(de2)&d1))
	elif code=='001':
		adj=choice(mol[fangmian][att]['1'])
		d=choice(list(set(de3)&d3))
	elif code=='101':
		adj=choice(mol[fangmian][att]['-1'])
		d=choice(list(set(de3)&d1))

	return formsen(att,d,adj)
def trans(h):
	if h=='-1 1':
		return '110'
	elif h=='-1 2':
		return '011'
	elif h=='-1 3':
		return '101'
	elif h=='0 1':
		return '000'
	elif h=='0 2':
		return '111'
	elif h=='1 1':
		return '100'
	elif h=='1 2':
		return '010'
	elif h=='1 3':
		return '001'
	

def decode(sen):
	global imol
	for item in blank:
		if sen in item:
			return 'eos'
	has=0
	for item in imol.keys():
		sp=item.split()
		if sp[0].encode('utf-8') in sen and sp[1].encode('utf-8') in sen:
			h=imol[item]
			has=1
			break
	if has==0:
		return ''
	
	flag=0
	for item in de1:
		if flag==1:
			break
		sp=item.split()
		for s in sp:
			if s not in sen:
				break
			flag=1
		if flag==1:
			h+=' 1'
	for item in de2:
		if item=='':
			continue
		if flag==1:
			break
		sp=item.split()
		for s in sp:
			if s not in sen:
				break
			flag=1
		if flag==1:
			h+=' 2'
	for item in de3:
		if flag==1:
			break
		sp=item.split()
		for s in sp:
			if s not in sen:
				break
			flag=1
		if flag==1:
			h+=' 3'	
	if flag==0:
		h+=' 2'
	code=trans(h)
	return code



