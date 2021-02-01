
from os import system, name

from time import sleep
from ClearScreenEffect import *

from chapterReader import *

from chapterEvent import *

#	Renderer class.
#	This is the class that handles the output.

class Renderer:
	
    def __init__(self):
    
        self.newStr = ""
        self.sleepSpeed = 0.005
        self.writeSpeed = 0.03
        self.lineSpeed = 1
        
    def ClearScreen(self):
        os = ""
        #	For windows:
        if name == "nt":
            os = system("cls")
        #	For mac etc
        else:
            os = system("clear")
            
    def DisplayFullChapter(self, lines, chapter):
    
        print(chapter.chapterTitle)
    
        story = ""
        
        #   Output.
        for line in lines:
        
            #   Only occur if line is 
            if "	//evt" in line:
            
                print("has found event in story!")
                args = [1, 10]
                
                if isinstance(chapter.chapterEvent, ChapterEventOBJ):
                    chapter.chapterEvent.ExecuteEvent(args)
                    self.ClearScreen()
                else:
                    print("Sorry, no chapter event!")
                    
            else:
                self.DisplaySinlgeLine(line, story, self.writeSpeed)
                
            sleep(self.lineSpeed)
            story += line
            self.ClearScreen() 

    #   Writes to the screen.
    def DisplaySinlgeLine(self, theString, story, timeSeconds):
    
        for letter in theString:
            self.ClearScreen()
            sleep(self.sleepSpeed)
            self.newStr += letter
            print(self.newStr)

	