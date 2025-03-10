#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : CuiDisplay.py
# 制作			 : tatra 2024年11月17日
# 対象バージョン : python 3.x. 以上
# version 		 : '0.0.1'
# 
#
#
# メモ :
#
# ---------------------------------------------------------------------------
# 外部モジュール : 
# ---------------------------------------------------------------------------
############################################################
import math
import shutil
import os
#from Coor import Size

if __name__ == "__main__":
	from debug import debug, LogLevel
	from Coor import *
else :
	from .debug import debug, LogLevel
	from .Coor import *


class Color:
	class BG: # (背景)
		BLACK       = '\033[40m'#黒
		RED         = '\033[41m'#赤
		GREEN       = '\033[42m'#緑
		YELLOW      = '\033[43m'#黄
		BLUE        = '\033[44m'#青
		MAGENTA     = '\033[45m'#マゼンタ
		CYAN        = '\033[46m'#シアン
		WHITE       = '\033[47m'#白

		BLACKr      = '\033[100m'#明るい黒（グレー）
		REDr        = '\033[101m'#明るい赤
		GREENr      = '\033[102m'#明るい緑
		YELLOWr     = '\033[103m'#明るい黄
		BLUEr       = '\033[104m'#明るい青
		MAGENTAr    = '\033[105m'#明るいマゼンタ
		CYANr       = '\033[106m'#明るいシアン
		WHITEr      = '\033[107m'#明るい白

		DEFAULT     = '\033[49m'#背景色をデフォルトに戻す

	class FG: #(文字)
		BLACK          = '\033[30m'#黒
		RED            = '\033[31m'#赤
		GREEN          = '\033[32m'#緑
		YELLOW         = '\033[33m'#黄
		BLUE           = '\033[34m'#青
		MAGENTA        = '\033[35m'#マゼンタ
		CYAN           = '\033[36m'#シアン
		WHITE          = '\033[37m'#白

		BLACKr         = '\033[90m'#明るい黒（グレー）
		REDr           = '\033[91m'#明るい赤
		GREENr         = '\033[92m'#明るい緑
		YELLOWr        = '\033[93m'#明るい黄
		BLUEr          = '\033[94m'#明るい青
		MAGENTAr       = '\033[95m'#明るいマゼンタ
		CYANr          = '\033[96m'#明るいシアン
		WHITEr         = '\033[97m'#明るい白

		DEFAULT        = '\033[39m'#文字色をデフォルトに戻す
	class CT:
		BOLD           = '\033[1m'#太字
		UNDERLINE      = '\033[4m'#下線
		INVISIBLE      = '\033[08m'#不可視
		REVERCE        = '\033[07m'#文字色と背景色を反転
		RESET          = '\033[0m'#全てリセット


class DrawStatus:
	OK=0
	UnderConsoleSize=1

class SelectMode:
	CheckBox=0
	SelectBox=1
	TextBg=2

#class ClUiObje

class ClUiObje():
	pass

class ClUiObje():
	bg_color:Color.BG = Color.BG.BLUE
	base_text_color:Color.FG = Color.FG.BLACK
	def __init__(self) -> None:
		self.child:ClUiObje=[]
		self.parent:ClUiObje
		self.rect:Rect
		return

	def getSize(self)-> Size:
		return self.rect.getSize()

	def getRect(self)->Rect:
		return self.rect
	
	def __addParent(self,parent:ClUiObje):
		self.parent = parent
		return
	
	def addChild(self, child:ClUiObje):
		child.__addParent(self)
		self.child.append(child)
		return
	def update_color(self):
		print(self.bg_color + self.base_text_color,end="")
	def reset_color(self):
		print(Color.CT.RESET,end="")
	def draw_print(self,str):
		print(str,end="")

	def update(self):
		for o in self.child:
			o.update()
	def draw(self, in_CanvasSize:Size, in_Point:Point)->int:
		x=0
		for child in self.child:
			x+=child.draw(in_CanvasSize,in_Point)
			if x != 0:
				continue
		return x


class ConsoleUserInterface_base():
	select_color:Color.BG = Color.BG.BLUE
	selector_color:Color.BG = Color.BG.RED
	select_text_color:Color.FG = Color.FG.WHITEr
	"""
		┌───────────────────
		│┌──────────────────
		││┌──────────────────
		│││↑[ ] 
		│││  [*]
		│││↓[ ]
		││└──────────────────
		│└──────────────────
		└───────────────────
	"""

	
	def __init__(self) -> None:
		self.obj:ClUiObje=[]
		self.updateSize()
		return

	def addChild(self,child:ClUiObje):
		self.obj.append(child)
		return
	
	def updateSize(self)->os.terminal_size:
		size = shutil.get_terminal_size()
		self.size=Size(size)-1
		return size

	def draw(self)-> DrawStatus:
		size=self.updateSize()
	
		columns = size.columns-1
		lines = size.lines-1
		for o in self.obj:
			o.update(Rect(Point(0,0),Size(columns,lines)))
		#if (columns < self.size_w_min) :
		#	return DrawStatus.UnderConsoleSize
		#if (lines < self.console_size_h_min) :
		#	return DrawStatus.UnderConsoleSize

		h = 0
		while( h <= lines):
			w = 0
			while( w <= columns):
				for o in self.obj:
					w += o.draw(Size( lines , columns ),Point(w,h))
			h+=1

if __name__ == "__main__":
	#debug.set_level(LogLevel.ALL)
	debug.set_level(LogLevel.ALL)
	CUI = ConsoleUserInterface_base()
	CUI.draw()
	input()

