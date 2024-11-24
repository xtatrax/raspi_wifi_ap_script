#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################################################
# file			 : setup.py
# 制作			 : tatra 2024年11月12日
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

import argparse
import enum
from tlib.debug import debug, LogLevel
from tlib import LanguageWrapper
"""
def thread_arg_type(string):
    value = int(string)
    if value < 0:
        msg = "無効なスレッド数(%d)" % string
        raise argparse.ArgumentTypeError(msg)
    return value
parser = argparse.ArgumentParser(description=u'簡単な例です') # parserを作る
parser.add_argument('bar')         # 引数を追加します
parser.add_argument('-f', '--foo') # オプションを追加します
parser.add_argument('-r', required=True) # このオプションは必須です
parser.add_argument('--version', action='version', version='%(prog)s 0.0.1') # version
parser.add_argument('-t', '--thread',type=thread_arg_type,default=1, help=u'スレッド数(0=自動,デフォルト=1)')
parser.add_argument('-i', '--ignore', action='store_true', help=u' --l を除外リストとして解釈します｡') #

group = parser.add_mutually_exclusive_group()
group.add_argument('-a','--ora', help=u'または --orb')
group.add_argument('-b','--orb', help=u'または --ora')

subparsers = parser.add_subparsers(help=u'help for subcommand')

parser_a = subparsers.add_parser('command_1', help=u'command_1 help')
parser_a.add_argument('-c', type=str,required=True, help=u'help for bar, positional')
parser_a.add_argument('-d', type=str,required=True, help=u'help for bar, positional')

parser_b = subparsers.add_parser('command_2', help=u'help for command_2')
parser_b.add_argument('-e', type=str,required=True, help=u'help for b')
parser_b.add_argument('-f', type=str,required=True, action='store', default='', help=u'test')
args = parser.parse_args() # コマンドラインの引数を解釈します
"""

@enum.unique
class UIMode(enum.IntEnum):
	NUM = 0
	CUI = 1
	GUI = 2

def __show_Lang_Select_UI_NUM__(langWap:LanguageWrapper.LangWap):
	llist = langWap.getLangList()
	langlist=[]
	i=0
	for l in llist:
		lc=llist[l]["LanguageCode"]
		langlist.append(lc)
		print(" {: >2}".format(i) + " : " + lc + " -> " + llist[l]["Description"])
		i+=1
	#debug.dprint(langlist)
	while (True):
		i_val = input(langWap.getMessage("lanSelectInfo"))
		try:
			i_val = int(i_val)
		except:
			print(langWap.getMessage("invalidValue"))
			continue
		if (not ( 0 < i_val < i )):
			print(langWap.getMessage("invalidValue"))
			continue
		else :
			break
	langWap.loadLang(langlist[i_val])


def __show_Lang_Select_UI_CUI__(langWap:LanguageWrapper.LangWap):
	raise Exception("未実装")
def __show_Lang_Select_UI_GUI__(langWap:LanguageWrapper.LangWap):
	raise Exception("please Override")

def showLangSelectUI(langWap:LanguageWrapper.LangWap, mode:UIMode=UIMode.NUM):
	match mode:
		case UIMode.NUM:
			__show_Lang_Select_UI_NUM__(langWap)
		case UIMode.CUI:
			__show_Lang_Select_UI_CUI__(langWap)
		case UIMode.GUI:
			__show_Lang_Select_UI_GUI__(langWap)

if __name__ == "__main__":
	#debug.set_level(LogLevel.ALL)
	langWap = LanguageWrapper.LangWap()
	llist = langWap.getLangList()
	debug.dprint(llist)

	showLangSelectUI(langWap)
