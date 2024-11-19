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

#from Coor import Size

if __name__ == "__main__":
	from debug import debug, LogLevel
	from Coor import *
else :
	from .debug import debug, LogLevel
	from .Coor import *


terminal_size = shutil.get_terminal_size()
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

		COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
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
	def __init__(self) -> None:
		self.child:ClUiObje=[]
		self.parent:ClUiObje
		self.rect:Rect
		return

	def getSize(self)-> Size:
		return self.rect.getSize()

	def __addParent(self,parent:ClUiObje):
		self.parent = parent
		return
	
	def addChild(self, child:ClUiObje):
		child.__addParent(self)
		self.child.append(child)
		return

	def update(self):
		for o in self.child:
			o.update()
	def draw(self, in_CanvasSize:Size, in_Point:Point)->int:
		x=0
		for child in self.child:
			x+=child.draw(in_CanvasSize,in_Point)
		return x

class World(ClUiObje):
	bg_color:Color.BG = Color.BG.BLUE
	base_text_color:Color.FG = Color.FG.BLACK
	def __init__(self, rect:Rect) -> None:
		super().__init__()
		self.rect=rect
		return

	def getSize(self)->Size:
		return self.rect.getSize()
	def update(self,rect:Rect):

		for o in self.child:
			o.update()
	def draw(self, in_CanvasSize:Size, in_Point:Point)->int:
		num=in_Point.x%10
		m = self.bg_color + str(num) + Color.CT.RESET
		x=0
		for child in self.child:
			x += child.draw(in_CanvasSize,in_Point)
			if x != 0:
				continue

		print(m,end="")
		if in_Point.x == in_CanvasSize.h:
			print("\n")
		x+=1
		return x

class Window(ClUiObje):
	color:Color.BG = Color.BG.WHITE

	margin_par = 3 # %
	margin_min = 1 # char
	padding_par = 0 # %
	padding_min = 2 # char
	size_h_min = 7 # char
	size_w_min = 20 # char

	size_min:Size=Size( size_h_min + margin_min + margin_min
					  ,	size_w_min + margin_min + margin_min)

	def __init__(self) -> None:
		super().__init__()

	def getSize(self) -> Size:
		return self.rect.getSize()

	def update(self):
		size = self.parent.getSize()

		wmh = math.floor( size.h * (self.margin_par / 100) )
		w_margin_h =  wmh if ( wmh > self.margin_min ) else self.margin_min

		wmw = math.floor( size.w * (self.margin_par / 100) )
		w_margin_w =  wmw if ( wmw > self.margin_min ) else self.margin_min

		self.size = Size(w_margin_w,w_margin_h)

		for o in self.child:
			o.update()

	def draw(self, in_ConsSize:Size, in_Point:Point)->int:
		self.getSize()
		x = 0
		for o in self.child:
			x += o.draw(in_ConsSize,in_Point)
		return x

class WindowFrame(ClUiObje):
	def getSize(self) -> Size:
		self.size = self.parent.getSize()
		return self.size

	def update(self):
		pass
	def draw(self, in_ConsSize:Size, in_Point:Point)->int:
		x = 0
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
		
		rect = Rect( 0, 0, terminal_size.columns, terminal_size.lines)
		world=World(rect)
		window=Window()
		world.addChild(window)
		self.addChild(world)
		return

	def addChild(self,child:ClUiObje):
		self.obj.append(child)
		return
	
	def draw(self)-> DrawStatus:
		columns = terminal_size.columns
		lines = terminal_size.lines
		for o in self.obj:
			o.update()
		#if (columns < self.size_w_min) :
		#	return DrawStatus.UnderConsoleSize
		#if (lines < self.console_size_h_min) :
		#	return DrawStatus.UnderConsoleSize

		#wmh = math.floor( lines * (self.window_margin_par / 100) )
		#w_margin_h =  wmh if ( wmh > self.window_margin_min ) else self.window_margin_min

		#wmw = math.floor( columns * (self.window_margin_par / 100) )
		#w_margin_w =  wmw if ( wmw > self.window_margin_min ) else self.window_margin_min

		h = 0
		while( h < lines):
			w = 0
			while( w < columns):
				for o in self.obj:
					w += o.draw(Size( lines , columns ),Point(w,h))
			h+=1
			"""
			num=w%10
			m = self.bg_color + str(num) + Color.CT.RESET

			ht = ( h >= w_margin_h )
			hb = ( h < (lines - w_margin_h) )
			wl = ( w > w_margin_w)
			wr = ( w < (columns - w_margin_w))
			if ( ( ht and hb )
			and	 ( wl and wr ) ) :
				c=" "
				if h == w_margin_h and w-1 == w_margin_w:
					c = "┌"
				elif h == w_margin_h and w+1 == (columns - w_margin_w):
					c = "┐"
				elif h+1 ==  (lines - w_margin_h) and w-1 == w_margin_w:
					c = "└"
				elif h+1 ==  (lines - w_margin_h) and w+1 == (columns - w_margin_w):
					c = "┘"
				elif h == w_margin_h or h+1 ==  (lines - w_margin_h):
					c = "─"
				elif w-1 == w_margin_w or w+1 == (columns - w_margin_w):
					c = "│"
				m = self.window_color + self.base_text_color + c + Color.CT.RESET
				print(m,end="")
				if w == columns:
					print("\n")
				continue
			"""
			
		

if __name__ == "__main__":
	#debug.set_level(LogLevel.ALL)
	debug.set_level(LogLevel.ALL)
	CUI = ConsoleUserInterface_base()
	CUI.draw()
	input()

"""
01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
0123456┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐456789
0123456│                                                                                                                                                                                         │456789
0123456│                                                                                                                                                                                         │456789
0123456│                                                                                                                                                                                         │456789
0123456│                                                                                                                                                                                         │456789
0123456│                                                                                                                                                                                         │456789
0123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456│                                                                                                                                                                                         │4567890123456└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘45678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
"""