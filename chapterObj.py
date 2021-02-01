
from chapterEvent import *

class ChapterOBJ:

	def __init__(self, indexNumber, chapterTitle, filePath):
		self.indexNumber = indexNumber
		self.chapterTitle = chapterTitle
		self.filePath = filePath
		self.chapterEvent = ""

	def AddEvent(self, evt):
		if isinstance(evt, ChapterEventOBJ):
			self.chapterEvent = evt
		else:
			print("Error: Object not Event Object")
    