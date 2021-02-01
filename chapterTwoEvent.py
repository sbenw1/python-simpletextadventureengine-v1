
import random 

#	Some dummy chapter event.
class ChapterTwoEvent:
	
	def ChapterEvent(self, args):
		return random.randint(args[0], args[1])