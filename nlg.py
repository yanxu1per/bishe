#!/usr/bin/python
# -*- coding: UTF-8 -*-

import codecs,chardet
import pdb
import re
from config import config
from utils import encode,formsen,decode
from random import choice,shuffle

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

#chexin=raw_input("Choose a car: ")
chexin='raw'
code=raw_input('Bit stream: ')
length=len(code)
if length%3==1:
	code=code+'00'
	length+=2
elif length%3==2:
	code+='0'
	length+=1
print code
f2=codecs.open('att7','r','utf-8')
text=''
text+=chexin.join(de0[0].split())+' '
#pdb.set_trace()
count=0
eos=0

for fangmian in mol.keys():
	#flag=0
	text+=fangmian.encode('utf-8')+de4[0]+' '
	for att in mol[fangmian]:
		if count>=length and eos==0:
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
sens=text.split()
result=''
for sen in sens:
	h=decode(sen)
	if h=='eos':
		break
	try:
		result+=h
	except:
		pdb.set_trace()
print result


