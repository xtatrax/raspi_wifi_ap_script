#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : coor.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月17日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.5'
# 説明			 :
#	座標系の定義
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################

import enum

class Algin(enum.Flag):
	top=enum.auto()
	bottom=enum.auto()
	left=enum.auto()
	right=enum.auto()

	top_left=top | left
	bottom_left=bottom |left
	top_right=top | right
	bottom_right=bottom | right

	w_middle=top | bottom
	h_middle=left | right

	center=w_middle | h_middle
	pass

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
	def __add__(self, other:Point):
		self.x += other.x
		self.y += other.y

	def __sub__(self, other:Point):
		self.x -= other.x
		self.y -= other.y

class Size():
	w=0
	h=0
	def __init__(self) -> None:
		"""
			Point()
		"""
	def __init__(self,point:Point) -> None:
		"""
			Point()
		"""
		self.w = point.x
		self.h = point.y
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
	base_point:Algin
	point:Point
	size:Size
	
	def __init__(self, x, y, h, w) -> None:
		"""

		"""
		self.point=Point(x,y)
		self.size=Size(h,w)
		self.base_point=Algin.top_left

	def __init__(self,begin:Point,end:Point) -> None:
		"""
		"""
		self.point=begin
		self.size=begin-end
		self.base_point=Algin.top_left

	def __init__(self,point:Point,size:Size,base_point:Algin) -> None:
		"""
		"""
		self.base_point=base_point
		self.point=point
		self.size=size
		# 寄せ定義して開始位置を算出

	def getSize(self)->Size:
		return self.size
	def getWide(self):
		return self.size.w
	def getHeight(self):
		return self.size.h
	def getBegin(self)->Point:
		return self.point
	def getBeginX(self):
		return self.point.x
	def getBeginY(self):
		return self.point.y
	def getEnd(self)->Point:
		return self.point + self.size
	def getEndX(self):
		return self.point.x + self.size.w
	def getEndY(self):
		return self.point.y + self.size.h



if __name__ == "__main__":
	rect = Rect(0,0,1,1)
