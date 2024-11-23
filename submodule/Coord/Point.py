#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : Point.py
# 推奨TABサイズ	 : 4
# 制作			 : tatra 2024年11月24日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.5'
# 説明			 :
#	座標系ポイントの定義
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################

from typing import overload
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from .Size import Size
if __name__ == "__main__":
	from debug import debug, LogLevel
else :
	from ..debug import debug, LogLevel

class Point():
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
	def __add__(self, other:'Size')->Point:
		pass
	def __add__(self, other)->Point:
		if type(other) is Point:
			return Point(self.x + other.x,self.y + other.y)
		elif type(other) is 'Size':
			return Point(self.x + other.w,self.y + other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
	@overload
	def __iadd__(self, other:Point)->Point:
		pass
	@overload
	def __iadd__(self, other:'Size')->Point:
		pass
	def __iadd__(self, other)->Point:
		if type(other) is Point:
			self.x += other.x
			self.y += other.y
			return self
		elif type(other) is 'Size':
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
		elif type(other) is 'Size':
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
		elif type(other) is 'Size':
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
	def __lt__(self, other:'Size'):
		pass
	def __lt__(self, other):
		if type(other) is Point:
			return (self.x < other.x and self.y < other.y)
		elif type(other) is 'Size':
			return (self.x < other.w and self.y < other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

	# self <= other
	@overload
	def __le__(self, other:Point):
		pass
	@overload
	def __le__(self, other:'Size'):
		pass
	def __le__(self, other):
		if type(other) is Point:
			return (self.x <= other.x and self.y <= other.y)
		elif type(other) is 'Size':
			return (self.x <= other.w and self.y <= other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

	# self == other
	@overload
	def __eq__(self, other:Point):
		pass
	@overload
	def __eq__(self, other:'Size'):
		pass
	def __eq__(self, other):
		if type(other) is Point:
			return (self.x == other.x and self.y == other.y)
		elif type(other) is 'Size':
			return (self.x == other.w and self.y == other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False


	# self != other
	@overload
	def __ne__(self, other:Point):
		pass
	@overload
	def __gt__(self, other:'Size'):
		pass
	def __gt__(self, other):
		if type(other) is Point:
			return not (self.x == other.x and self.y == other.y)
		elif type(other) is 'Size':
			return not (self.x == other.w and self.y == other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False

	# self > other
	@overload
	def __gt__(self, other:Point):
		pass
	@overload
	def __gt__(self, other:'Size'):
		pass
	def __gt__(self, other):
		if type(other) is Point:
			return (self.x > other.x and self.y > other.y)
		elif type(other) is 'Size':
			return (self.x > other.w and self.y > other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False


	# self >= other
	@overload
	def __ge__(self, other:Point):
		pass
	@overload
	def __ge__(self, other:'Size'):
		pass	
	def __ge__(self, other):
		if type(other) is Point:
			return (self.x >= other.x and self.y >= other.y)
		elif type(other) is 'Size':
			return (self.x >= other.w and self.y >= other.h)
		debug.cprint(str(type(other)) + "? そいつぁしらねぇなぁ?")
		return False
