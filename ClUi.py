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
from tlib.debug import debug, LogLevel
from tlib import LanguageWrapper
import tlib.CuiDisplay as CuiDsp

hexc="[0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]"
def debug1cN(num)->str:
	l = len(hexc)
	m = num % l
	return hexc[m]

class World(CuiDsp.ClUiObje):
	def __init__(self, rect:CuiDsp.Rect) -> None:
		self.bg_color:CuiDsp.Color.BG = CuiDsp.Color.BG.BLUE
		self.base_text_color:CuiDsp.Color.FG = CuiDsp.Color.FG.BLACK
		super().__init__()
		self.setRect(rect)
		return

	def getSize(self)->CuiDsp.Size:
		return self.rect.getSize()
	def update(self,rect:CuiDsp.Rect):
		self.setRect(rect)
		for o in self.child:
			o.update()
	def draw(self, in_CanvasSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:

		x=0
		for child in self.child:
			x += child.draw(in_CanvasSize,in_Point)
			if x != 0:
				continue

		self.update_color()
		if x == 0:
			c = " "
			if (( in_Point.x == in_CanvasSize.h )
			and ( in_Point.y != in_CanvasSize.w )):
				self.draw_print("\n")
			else:
				self.draw_print(debug1cN(in_Point.x))
			
			x+=1

		self.reset_color()
		return x

class Window(CuiDsp.ClUiObje):

	margin_par = 10 # %
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

		self.setRect(
			CuiDsp.Rect(
				start=CuiDsp.Point(x=w_margin_w,y=w_margin_h),
				end=CuiDsp.Point(x=size.w - w_margin_w, y=size.h - w_margin_h )
			), True )
		for o in self.child:
			o.update()

	def draw(self, in_CanvasSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:
		if not self.isInPoint(in_Point) :
			return 0

		x = 0
		self.update_color()

		x += super().draw(in_CanvasSize,in_Point)

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

	def draw(self, in_CanvasSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:
		x = 0
		wRect = self.getWorldRect()
		if (wRect.getBeginX() == in_Point.x) and (wRect.getBeginY() == in_Point.y):
			self.draw_print("┏")
			return 1
		elif (wRect.getEndX() == in_Point.x) and (wRect.getBeginY() == in_Point.y):
			self.draw_print("┓")
			return 1
		elif (wRect.getBeginX() == in_Point.x) and (wRect.getEndY() == in_Point.y):
			self.draw_print("┗")
			return 1
		elif (wRect.getEndX() == in_Point.x) and (wRect.getEndY() == in_Point.y):
			self.draw_print("┛")
			return 1
		elif ((wRect.getBeginX() == in_Point.x) or (wRect.getEndX() == in_Point.x)):
			self.draw_print("┃")
			return 1
		elif ((wRect.getBeginY() == in_Point.y) or (wRect.getEndY() == in_Point.y)):
			self.draw_print("━")
			return 1

		x += super().draw(in_CanvasSize,in_Point)

		return x

class DrawArea(CuiDsp.ClUiObje):

	m_BaceRect:CuiDsp.Rect
	isDebug=True
	def __init__(self, rect:CuiDsp.Rect=CuiDsp.Rect(x=2,y=2,w=-2,h=-2 , abs=False) ) -> None:
		super().__init__()
		self.m_BaceRect=rect
		if self.isDebug:
			self.bg_color = CuiDsp.Color.BG.GREENr


	def update(self):
		self.setRect(
			self.m_BaceRect,
			True
		)
		for o in self.child:
			o.update()
		pass
	def draw(self, in_CanvasSize:CuiDsp.Size, in_Point:CuiDsp.Point)->int:
		if not self.isInPoint(in_Point) :
			return 0

		x = 0
		if self.isDebug:
			self.update_color()

		x += super().draw(in_CanvasSize,in_Point)

		if self.isDebug:
			if x == 0:
				self.draw_print(" ")
				x+=1
		return x

class ConsoleUserInterface(CuiDsp.ConsoleUserInterface_base):
	def __init__(self) -> None:
		super().__init__()
		rect = CuiDsp.Rect( point=CuiDsp.Point(x=0, y=0), size=self.size)
		world=World(rect)
		window=Window()
		frame=WindowFrame()
		drawArea=DrawArea()
		frame.addChild(drawArea)
		window.addChild(frame)
		world.addChild(window)
		self.addChild(world)
