

import shutil

terminal_size = shutil.get_terminal_size()

lines = terminal_size.lines
columns = terminal_size.columns
#print(terminal_size[0])
# => columns と同じ結果
#print(terminal_size[1])
# => lines と同じ結果
#https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
class Color:
		BOLD           = '\033[1m'#太字
		UNDERLINE      = '\033[4m'#下線
		INVISIBLE      = '\033[08m'#不可視
		REVERCE        = '\033[07m'#文字色と背景色を反転
		FG_BLACK          = '\033[30m'#(文字)黒
		FG_RED            = '\033[31m'#(文字)赤
		FG_GREEN          = '\033[32m'#(文字)緑
		FG_YELLOW         = '\033[33m'#(文字)黄
		FG_BLUE           = '\033[34m'#(文字)青
		FG_MAGENTA        = '\033[35m'#(文字)マゼンタ
		FG_CYAN           = '\033[36m'#(文字)シアン
		FG_WHITE          = '\033[37m'#(文字)白
		FG_COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
		BG_BLACK       = '\033[40m'#(背景)黒
		BG_RED         = '\033[41m'#(背景)赤
		BG_GREEN       = '\033[42m'#(背景)緑
		BG_YELLOW      = '\033[43m'#(背景)黄
		BG_BLUE        = '\033[44m'#(背景)青
		BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
		BG_CYAN        = '\033[46m'#(背景)シアン
		BG_WHITE       = '\033[47m'#(背景)白
		BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す

		RESET          = '\033[0m'#全てリセット
 

def draw():
	for y in range(columns):
		for x in range(lines):
			testTest = Color.BG_YELLOW + " " + Color.RESET
			print(testTest,end="")


if __name__ == "__main__":
	draw()