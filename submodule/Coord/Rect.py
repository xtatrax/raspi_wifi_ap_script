#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : Rect.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月24日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.5'
# 説明			 :
#	座標系矩形の定義
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################


from typing import overload

from .Size import Size
from .Point import Point
from .Align import Align

if __name__ == "__main__":
	from debug import debug, LogLevel
else :
	from ..debug import debug, LogLevel

class Rect():
	pass
class Rect():
	m_base_point:Align
	m_point:Point
	m_size:Size
	m_isAbsolute:bool
	#@overload
	#def __init__(self,x:int,y:int,w:int,h:int):
	#	pass
	#@overload
	#def __init__(self,start:Point,end:Point)-> None:
	#	pass
	#def __init__(self,point:Point,size:Size,base_point:Align=Align.top_left) :
	#	"""

	#	"""
	#	self.base_point=base_point
	#	self.point=point
	#	self.size=size
	def __init__(self,start:Point=None,size:Size=None,**kwargs) :
		"""
			使い方
			1 start:Point, size:Size, [] / 描画開始地点, サイズ
			2 start:Point, end:Point / 描画開始地点, 描画終了地点
			3 point:Point, size:Size, [align:Align] / 描画地点, サイズ, 描画開始地点の設定
			4 x:int, y:int, w:int, h:int / x, y, w, h
		"""
		if start and size:
			self.m_point=start
			self.m_size=size
			self.m_base_point=Align.top_left
			self.m_isAbsolute=False
			pass
		elif start and kwargs.get("end"):
			self.m_point=start
			self.m_size=kwargs.get("end")
			self.m_base_point=Align.top_left
			self.m_isAbsolute=True
			pass
		elif kwargs.get("point") and size:
			if kwargs.get("align"):
				self.m_base_point=kwargs.align
			else:
				self.m_base_point=Align.top_left
			self.m_point=kwargs.point
			self.m_size=size
			self.m_isAbsolute=False
			pass
		elif kwargs.get("x") and kwargs.get("y") and kwargs.get("w") and kwargs.get("h"):
			self.m_point=Point(kwargs.x,kwargs.y)
			self.m_size=Size(kwargs.w,kwargs.h)
			self.m_base_point=Align.top_left
			self.m_isAbsolute=False
			pass
		else:
			raise Exception()

	@overload
	def __add__(self, other:Point)->Rect:
		pass
	@overload
	def __add__(self, other:Size)->Rect:
		pass
	@overload
	def __add__(self, other:int)->Rect:
		pass
	def __add__(self, other)->Rect:
		if type(other) is Point:
			return Rect(point=(self.m_point + other),size=self.m_size, align=self.m_base_point)
		elif type(other) is Size:
			return Rect(point=self.m_point,size=(self.m_size + other), align=self.m_base_point)
		elif type(other) is int:
			return Size(point=(self.m_point + other) , size=(self.m_size + other), align=self.m_base_point)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __sub__(self, other:Point)->Rect:
		pass
	@overload
	def __sub__(self, other:Point)->Rect:
		pass
	@overload
	def __sub__(self, other:int)->Rect:
		pass
	def __sub__(self, other)->Rect:
		if type(other) is Point:
			return Rect(point=(self.m_point - other),size=self.m_size, align=self.m_base_point)
		elif type(other) is Size:
			return Rect(point=self.m_point,size=(self.m_size - other), align=self.m_base_point)
		elif type(other) is int:
			return Size(point=(self.m_point - other) , size=(self.m_size - other), align=self.m_base_point)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")


	def isInPoint(self, point:Point):
		match self.m_base_point:
			case Align.top_left:
				if self.m_isAbsolute :
					return ((self.m_point <= point) and (point <= self.m_size))
				return ((self.m_point <= point) and (point <= (self.m_point - self.m_size)))
				pass
			case Align.top_right:
				debug.cprint("Not implemented  未実装")
				pass
			case Align.bottom_left:
				debug.cprint("Not implemented  未実装")
				pass
			case Align.bottom_right:
				debug.cprint("Not implemented  未実装")
				pass
		pass

	def isAbsolute(self)->bool:
		return self.m_isAbsolute
	def getSize(self)->Size:
		return self.m_size
	def getWide(self)->int:
		return self.m_size.w
	def getHeight(self)->int:
		return self.m_size.h
	def getBegin(self)->Point:
		return self.m_point
	def getBeginX(self)->int:
		return self.m_point.x
	def getBeginY(self)->int:
		return self.m_point.y
	def getEnd(self)->Point:
		if self.m_isAbsolute :
			return self.m_size
		return self.m_point + self.m_size
	def getEndX(self)->int:
		if self.m_isAbsolute :
			return self.m_size.x
		return self.m_point.x + self.m_size.w
	def getEndY(self)->int:
		if self.m_isAbsolute :
			return self.m_size.y
		return self.m_point.y + self.m_size.h
