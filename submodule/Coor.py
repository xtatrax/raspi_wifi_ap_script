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
	@overload
	def __add__(self, other:Point):
		pass
	@overload
	def __add__(self, other:Size):
		pass
	def __add__(self, other)->Point:
		if type(other) is Point:
			return Point(self.x + other.x,self.y + other.y)
		elif type(other) is Size:
			return Point(self.x + other.w,self.y + other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")

	@overload
	def __sub__(self, other:Point):
		pass
	@overload
	def __sub__(self, other:Point):
		pass
	def __sub__(self, other)->Point:
		if type(other) is Point:
			return Point(self.x - other.x,self.y - other.y)
		elif type(other) is Size:
			return Point( self.x - other.w, self.y - other.h)
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
	def __gt__(self, other:Size):
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
	base_point:Algin
	point:Point
	size:Size
	isAbsolute:bool
	#@overload
	#def __init__(self,x:int,y:int,w:int,h:int):
	#	pass
	#@overload
	#def __init__(self,start:Point,end:Point)-> None:
	#	pass
	#def __init__(self,point:Point,size:Size,base_point:Algin=Algin.top_left) :
	#	"""

	#	"""
	#	self.base_point=base_point
	#	self.point=point
	#	self.size=size
	def __init__(self,start:Point=None,size:Size=None,**kwargs) :
		"""
			使い方
			1 start:Point, size:Size / 描画開始地点, サイズ
			2 start:Point, end:Point / 描画開始地点, 描画終了地点
			3 point:Point, size:Size, algin:Algin / 描画地点, サイズ, 描画開始地点の設定
			4 x:int, y:int, w:int, h:int / x, y, w, h
		"""
		if start and size:
			self.point=start
			self.size=size
			self.base_point=Algin.top_left
			self.isAbsolute=False
			pass
		elif start and kwargs.get("end"):
			self.point=start
			self.size=kwargs.get("end")
			self.base_point=Algin.top_left
			self.isAbsolute=True
			pass
		elif kwargs.get("point") and size:
			if kwargs.get("algin"):
				self.base_point=kwargs.algin
			else:
				self.base_point=Algin.top_left
			self.point=kwargs.point
			self.size=size
			self.isAbsolute=False
			pass
		elif kwargs.get("x") and kwargs.get("y") and kwargs.get("w") and kwargs.get("h"):
			self.point=Point(kwargs.x,kwargs.y)
			self.size=Size(kwargs.w,kwargs.h)
			self.base_point=Algin.top_left
			self.isAbsolute=False
			pass
		else:
			raise Exception()
		
	def isInPoint(self, point:Point):
		match self.base_point:
			case Algin.top_left:
				if self.isAbsolute :
					return ((self.point <= point) and (point <= self.size))
				return ((self.point <= point) and (point <= (self.point - self.size)))
				pass
			case Algin.top_right:
				debug.cprint("Not implemented  未実装")
				pass
			case Algin.bottom_left:
				debug.cprint("Not implemented  未実装")
				pass
			case Algin.bottom_right:
				debug.cprint("Not implemented  未実装")
				pass
		pass

	def getSize(self)->Size:
		return self.size
	def getWide(self)->int:
		return self.size.w
	def getHeight(self)->int:
		return self.size.h
	def getBegin(self)->Point:
		return self.point
	def getBeginX(self)->int:
		return self.point.x
	def getBeginY(self)->int:
		return self.point.y
	def getEnd(self)->Point:
		if self.isAbsolute :
			return self.size
		return self.point + self.size
	def getEndX(self)->int:
		if self.isAbsolute :
			return self.size.x
		return self.point.x + self.size.w
	def getEndY(self)->int:
		if self.isAbsolute :
			return self.size.y
		return self.point.y + self.size.h



if __name__ == "__main__":
	rect = Rect(Point(1,2),Point(3,4))
	pass