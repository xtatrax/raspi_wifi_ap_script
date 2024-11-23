
import enum

@enum.unique
class LogLevel(enum.Flag):
	NONE= enum.auto()
	INFO = enum.auto()
	DEBUG = enum.auto()
	WARNING = enum.auto()
	ERROR = enum.auto()
	EX_IGNORE = enum.auto()
	CRITICAL = enum.auto()
	ALL = INFO | DEBUG | WARNING | ERROR | CRITICAL


class debug():
	global logLevel
	logLevel=0

	def get_isDEBUG():
		global logLevel
		return (LogLevel.DEBUG in logLevel)

	def set_level(level:LogLevel):
		global logLevel
		logLevel = level

	def print(comment, ll:LogLevel=LogLevel.ALL):
		global logLevel
		if logLevel in ll:
			print(comment)
	
	def dprint(comment):
		global logLevel
		if (LogLevel.DEBUG in logLevel):
			print(comment)

	def iprint(comment):
		global logLevel
		if (LogLevel.INFO in logLevel):
			print(comment)

	def wprint(comment):
		global logLevel
		if (LogLevel.WARNING in logLevel):
			print(comment)

	def eprint(comment):
		global logLevel
		if (LogLevel.ERROR in logLevel):
			print(comment)

	def cprint(comment):
		global logLevel
		if not (LogLevel.EX_IGNORE in logLevel):
			raise Exception(comment)
		if (LogLevel.CRITICAL in logLevel):
			print(comment)
