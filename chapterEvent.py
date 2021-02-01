
#	The event object.
class ChapterEventOBJ:

	def __init__(self, evt):
		self.chapterEvent = evt
	       
    #   Executes the chapter event.
    #   EVT is the function that contains the actual logic of the 
    #   chapter's event. 
    #   ARGS are the arguments
	def ExecuteEvent(self, args):
		self.eventResults = self.chapterEvent(args)