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
import uuid
import os
from typing import overload
if __name__ == "__main__":
	from debug import debug, LogLevel
else :
	from .debug import debug, LogLevel

class Align(enum.Flag):
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
	@overload
	def __add__(self, other:Point)->Point:
		pass
	@overload
	def __add__(self, other:Size)->Point:
		pass
	def __add__(self, other)->Point:
		if type(other) is Point:
			return Point(self.x + other.x,self.y + other.y)
		elif type(other) is Size:
			return Point(self.x + other.w,self.y + other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
	@overload
	def __iadd__(self, other:Point)->Point:
		pass
	@overload
	def __iadd__(self, other:Size)->Point:
		pass
	def __iadd__(self, other)->Point:
		if type(other) is Point:
			self.x += other.x
			self.y += other.y
			return self
		elif type(other) is Size:
			self.x += other.w
			self.y += other.h
			return self
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __sub__(self, other:Point)->Point:
		pass
	@overload
	def __sub__(self, other:Point)->Point:
		pass
	def __sub__(self, other)->Point:
		if type(other) is Point:
			return Point(self.x - other.x,self.y - other.y)
		elif type(other) is Size:
			return Point( self.x - other.w, self.y - other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __isub__(self, other:Point)->Point:
		pass
	@overload
	def __isub__(self, other:Point)->Point:
		pass
	def __isub__(self, other)->Point:
		if type(other) is Point:
			self.x -= other.x
			self.y -= other.y
			return self
		elif type(other) is Size:
			self.x -= other.w
			self.y -= other.h
			return self
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	#__lt__(self, other)	self < other
	#__le__(self, other)	self <= other
	#__eq__(self, other)	self == ohter
	#__ne__(self, other)	self != other
	#__gt__(self, other)	self > other
	#__ge__(self, other)	self >= other

	# self < other
	@overload
	def __lt__(self, other:Point):
		pass
	@overload
	def __lt__(self, other:Size):
		pass
	def __lt__(self, other):
		if type(other) is Point:
			return (self.x < other.x and self.y < other.y)
		elif type(other) is Size:
			return (self.x < other.w and self.y < other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

	# self <= other
	@overload
	def __le__(self, other:Point):
		pass
	@overload
	def __le__(self, other:Size):
		pass
	def __le__(self, other):
		if type(other) is Point:
			return (self.x <= other.x and self.y <= other.y)
		elif type(other) is Size:
			return (self.x <= other.w and self.y <= other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

	# self == other
	@overload
	def __eq__(self, other:Point):
		pass
	@overload
	def __eq__(self, other:Size):
		pass
	def __eq__(self, other):
		if type(other) is Point:
			return (self.x == other.x and self.y == other.y)
		elif type(other) is Size:
			return (self.x == other.w and self.y == other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False


	# self != other
	@overload
	def __ne__(self, other:Point):
		pass
	@overload
	def __gt__(self, other:Size):
		pass
	def __gt__(self, other):
		if type(other) is Point:
			return not (self.x == other.x and self.y == other.y)
		elif type(other) is Size:
			return not (self.x == other.w and self.y == other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

	# self > other
	@overload
	def __gt__(self, other:Point):
		pass
	@overload
	def __gt__(self, other:Size):
		pass
	def __gt__(self, other):
		if type(other) is Point:
			return (self.x > other.x and self.y > other.y)
		elif type(other) is Size:
			return (self.x > other.w and self.y > other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False


	# self >= other
	@overload
	def __ge__(self, other:Point):
		pass
	@overload
	def __ge__(self, other:Size):
		pass	
	def __ge__(self, other):
		if type(other) is Point:
			return (self.x >= other.x and self.y >= other.y)
		elif type(other) is Size:
			return (self.x >= other.w and self.y >= other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

class Size():
	w=0
	h=0
	def __init__(self) -> None:
		pass
	@overload
	def __init__(self,point:Size) -> None:
		pass
	@overload
	def __init__(self,point:Point) -> None:
		pass
	@overload
	def __init__(self,size:os.terminal_size) -> None:
		pass
	@overload
	def __init__(self,w:int,h:int) -> None:
		pass
	def __init__(self, arg1, arg2=None) -> None:
		if type(arg1) is int:
			if type(arg2) is int:
				self.w = arg1
				self.h = arg2
				return
			debug.iprint(" please if ( (type(arg1) is int) and (type(arg2) is int))")
			debug.cprint("if arg1 is int case of arg2 is int please")

		elif type(arg1) is Point:
			self.w = arg1.x
			self.h = arg1.y
			return
		elif type(arg1) is Size:
			self.w = arg1.w
			self.h = arg1.h
			return
		elif type(arg1) is os.terminal_size:
			self.w = arg1.columns
			self.h = arg1.lines
			return


	@overload
	def __add__(self, other:Point)->Size:
		pass
	@overload
	def __add__(self, other:Size)->Size:
		pass
	@overload
	def __add__(self, other:int)->Size:
		pass
	def __add__(self, other)->Size:
		if type(other) is Point:
			return Size(self.w + other.x,self.h + other.y)
		elif type(other) is Size:
			return Size(self.w + other.w,self.h + other.h)
		elif type(other) is int:
			return Size(self.w + other, self.h + other)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __iadd__(self, other:Point)->Size:
		pass
	@overload
	def __iadd__(self, other:Size)->Size:
		pass
	@overload
	def __iadd__(self, other:int)->Size:
		pass
	def __iadd__(self, other)->Size:
		if type(other) is Point:
			self.w += other.x
			self.h += other.y
			return self
		elif type(other) is Size:
			self.w += other.w
			self.h += other.h
			return self
		elif type(other) is int:
			self.w += other
			self.h += other
			return self
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __sub__(self, other:Point)->Size:
		pass
	@overload
	def __sub__(self, other:Point)->Size:
		pass
	@overload
	def __sub__(self, other:int)->Size:
		pass
	def __sub__(self, other)->Size:
		if type(other) is Point:
			return Size(self.w - other.x, self.h - other.y)
		elif type(other) is Size:
			return Point(self.w - other.w, self.h - other.h)
		elif type(other) is int:
			return Point(self.w - other, self.h - other)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __isub__(self, other:Point)->Size:
		pass
	@overload
	def __isub__(self, other:Point)->Size:
		pass
	@overload
	def __isub__(self, other:int)->Size:
		pass
	def __isub__(self, other)->Size:
		if type(other) is Point:
			self.w -= other.x
			self.h -= other.y
			return self
		elif type(other) is Size:
			self.w -= other.w
			self.h -= other.h
			return self
		elif type(other) is int:
			self.w -= other
			self.h -= other
			return self
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	# self < other
	def __lt__(self, other:Point):
		return (self.w < other.x and self.h < other.y)
	def __lt__(self, other:Size):
		return (self.w < other.w and self.h < other.h)
	# self <= other
	def __le__(self, other:Point):
		return (self.w <= other.x and self.h <= other.y)
	def __le__(self, other:Size):
		return (self.w <= other.w and self.h <= other.h)
	# self == other
	def __eq__(self, other:Point):
		return (self.w == other.x and self.h == other.y)
	def __eq__(self, other:Size):
		return (self.w == other.w and self.h == other.h)
	# self != other
	def __ne__(self, other:Point):
		return not (self.w == other.x and self.h == other.y)
	def __ne__(self, other:Size):
		return not (self.w == other.w and self.h == other.h)
	# self > other
	def __gt__(self, other:Point):
		return (self.w > other.x and self.h > other.y)
	def __gt__(self, other:Size):
		return (self.w > other.w and self.h > other.h)
	# self >= other
	def __ge__(self, other:Point):
		return (self.w >= other.x and self.h >= other.y)
	def __ge__(self, other:Size):
		return (self.w >= other.w and self.h >= other.h)

class Vector():
	l=0
	r=0

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



if __name__ == "__main__":
	rect = Rect(Point(1,2),Point(3,4))
	pass