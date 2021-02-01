
#	The init
#	Where everything comes together.

from time import sleep

#   Custom objects 
from chapterObj import * 
from chapterRegistry import *

from chapterEvent import *

from chapterTwoEvent import *

#   Start the game.
def StartGame():

    
    #   The source of the text file.
    src = "D:/Docs/Portfolio/2020/may-2020/software-works/python/simple-text-adventure/chapters/chapter1.txt"
    #src = "chapter1.txt"
    
    #   A chapter registry.
    Registry = ChapterRegistry()
    
    c1 = ChapterOBJ(1, "PART ONE", "D:/Docs/Portfolio/2020/may-2020/software-works/python/simple-text-adventure/chapters/chapter1.txt")
    c2 = ChapterOBJ(2, "PART TWO", "D:/Docs/Portfolio/2020/may-2020/software-works/python/simple-text-adventure/chapters/chapter2.txt")
    
    c2Event = ChapterTwoEvent()
    c2EventOBJ = ChapterEventOBJ(c2Event.ChapterEvent)
    
    #   Add Chapter 1
    Registry.AddChapter(c1)
    
    #   Add the event to chapter 2
    c2.AddEvent(c2EventOBJ)
    
    #   Add chapter 2
    Registry.AddChapter(c2)
    
    Registry.DisplayStory()

        
StartGame()
