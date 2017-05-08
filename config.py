#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs,chardet
class config:
	def __init__(self):
		self.de0=['说起 这款车']
		self.de1=['还算','只能说','勉强谈得上','偏','略显']
		self.de2=['的确','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉']
		self.de3=['非常','很','特别','真是','超级','给人非常 的感觉','过于','太过']

		self.d1=set(['偏','过于','太过','略显','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','很','特别','真是','只能说'])
		self.d2=set(['勉强谈得上','比较','给人一种 的感觉','让我觉得','有一股 的感觉','','有些','感觉','感觉 吧','非常','很','真是','超级','给人非常 的感觉'])
		self.d3=set(['非常','很','特别','真是','超级','给人非常 的感觉','给人一种 的感觉','让我觉得','','有些','感觉','勉强谈得上','的确','比较'])
		self.de4=['方面']
		self.blank=['其他的呢','再有呢','和我之前那一辆车比起来','还算不错 毕竟咱也不是专业车手','个人觉得还算满意','买了之后没有什么太大的遗憾','还是家人觉得好就好','我也不奢求太多']
	def formmol(self):
		f=codecs.open('dataset2','r','utf-8')	
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
		return mol
	def formimol(self):
		f=codecs.open('dataset2','r','utf-8')
		imol={}
		lines=f.readlines()
		for line in lines:
			sp=line.split()	
			imol[' '.join(sp[1:3])]=sp[3]
		return imol
