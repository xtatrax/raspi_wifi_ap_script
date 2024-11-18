#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : coor.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月17日
# 対象バージョン : python 3.x. 以上
# version 		 : '0.0.1'
# 説明			 :
#	座標系の定義
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################



class Point():
	pass
class Size():
	pass
class Vector():
	pass
class Rect():
	pass

class Point():
	x=0
	y=0
	def __init__(self) -> None:
		"""
			Point()
		"""

	def __init__(self,x,y) -> None:
		"""
			Point(x,y)
		"""
		self.x = x
		self.y = y

class Size():
	w=0
	h=0
	def __init__(self) -> None:
		"""
			Point()
		"""

	def __init__(self,w,h) -> None:
		"""
			Size(w,h)
		"""
		self.w = w
		self.h = h

class Vector():
	l=0
	r=0

class Rect():
	begin:Point
	size:Size
	point:Point
	def __init__(self,x,y,h,w):
		pass
	def __init__(self,begin,end):
	    pass
	def __init__(self,point,size):
		pass
	def getSize(self):
		pass
	def getWide(self):
		pass
	def getHeight(self):
		pass
	def getBegin(self):
		pass
	def getBeginX(self):
		pass
	def getBeginY(self):
		pass
	def getEnd(self):
		pass
	def getEndX(self):
		pass
	def getEndY(self):
		pass



