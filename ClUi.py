#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : test.py
# 制作			 : tatra 2024年11月23日
# 対象バージョン : python 3.10. 以上
# version 		 : '0.0.1'
# 
#
#
# メモ :
#
#""" Details about the module and for what purpose it was built for"""
# ---------------------------------------------------------------------------
# 外部モジュール : chardet
# ---------------------------------------------------------------------------
############################################################
import math
from submodule.debug import debug, LogLevel
from submodule import LanguageWrapper
import submodule.CuiDisplay as CuiDsp

class World(CuiDsp.ClUiObje):
	def __init__(self, rect:CuiDsp.Rect) -> None:
		self.bg_color:CuiDsp.Color.BG = CuiDsp.Color.BG.BLUE
		self.base_text_color:CuiDsp.Color.FG = CuiDsp.Color.FG.BLACK
		super().__init__()
		self.rect=rect
		return

	def getSize(self)->CuiDsp.Size:
		return self.rect.getSize()
	def update(self,rect:CuiDsp.Rect):
		self.rect=rect
		for o in self.child:
			o.update()
	def draw(self, in_CanvasSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:
		num=in_Point.x%10

		x=0
		for child in self.child:
			x += child.draw(in_CanvasSize,in_Point)
			if x != 0:
				continue

		self.update_color()
		if x == 0:
			self.draw_print(num)
			x+=1
		#if in_Point.x == in_CanvasSize.h:
		#	print("\n")
		self.reset_color()
		return x

class Window(CuiDsp.ClUiObje):

	margin_par = 3 # %
	margin_min = 1 # char
	padding_par = 0 # %
	padding_min = 2 # char
	size_h_min = 7 # char
	size_w_min = 20 # char

	size_min:CuiDsp.Size=CuiDsp.Size( size_h_min + margin_min + margin_min
					  ,	size_w_min + margin_min + margin_min)

	def __init__(self) -> None:
		self.bg_color:CuiDsp.Color.BG = CuiDsp.Color.BG.WHITE
		self.base_text_color = CuiDsp.Color.FG.BLACK
		super().__init__()

	def getSize(self) -> CuiDsp.Size:
		return self.rect.getSize()

	def update(self):
		size = self.parent.getSize()

		wmh = math.floor( size.h * (self.margin_par / 100) )
		w_margin_h =  wmh if ( wmh > self.margin_min ) else self.margin_min

		wmw = math.floor( size.w * (self.margin_par / 100) )
		w_margin_w =  wmw if ( wmw > self.margin_min ) else self.margin_min

		self.rect = CuiDsp.Rect(CuiDsp.Point(w_margin_w,w_margin_h), end=CuiDsp.Point(size.w - w_margin_w, size.h - w_margin_h ))
		for o in self.child:
			o.update()

	def draw(self, in_ConsSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:
		if not self.rect.isInPoint(in_Point) :
			return 0

		x = 0
		self.update_color()
		for o in self.child:
			x += o.draw(in_ConsSize,in_Point)
			if x != 0:
				continue
		if x == 0:
			self.draw_print(" ")
			x+=1
		return x

class WindowFrame(CuiDsp.ClUiObje):
	def getSize(self) -> CuiDsp.Size:
		self.size = self.parent.getSize()
		return self.size

	def update(self):
		parent_rect = self.parent.getRect()
		self.rect = parent_rect
		for o in self.child:
			o.update()

	def draw(self, in_ConsSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:
		x = 0
		endx=self.rect.getEndX()
		if (self.rect.getBeginX() == in_Point.x) and (self.rect.getBeginY() == in_Point.y):
			self.draw_print("┏")
			x+=1
		elif (self.rect.getEndX() == in_Point.x) and (self.rect.getBeginY() == in_Point.y):
			self.draw_print("┓")
			x+=1
		elif (self.rect.getBeginX() == in_Point.x) and (self.rect.getEndY() == in_Point.y):
			self.draw_print("┗")
			x+=1
		elif (self.rect.getEndX() == in_Point.x) and (self.rect.getEndY() == in_Point.y):
			self.draw_print("┛")
			x+=1
		elif ((self.rect.getBeginX() == in_Point.x) or (self.rect.getEndX() == in_Point.x)):
			self.draw_print("┃")
			x+=1
		elif ((self.rect.getBeginY() == in_Point.y) or (self.rect.getEndY() == in_Point.y)):
			self.draw_print("━")
			x+=1

		return x




class ConsoleUserInterface(CuiDsp.ConsoleUserInterface_base):
	def __init__(self) -> None:
		super().__init__()
		rect = CuiDsp.Rect( CuiDsp.Point(0, 0), self.size)
		world=World(rect)
		window=Window()
		frame=WindowFrame()
		window.addChild(frame)
		world.addChild(window)
		self.addChild(world)
