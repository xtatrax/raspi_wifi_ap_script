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
from tlib.debug import debug, LogLevel
from tlib import LanguageWrapper
from tlib.CuiDisplay import ConsoleUserInterface_base
import ClUi

if __name__ == "__main__":
	debug.set_level(LogLevel.ALL)
	CUI = ClUi.ConsoleUserInterface()
	CUI.draw()
	#input()
