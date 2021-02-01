
from chapterObj import *

from ReadFile import *
from chapterReader import *
from ScreenWriter import * 
from ClearScreenEffect import *
from renderer import *

#	Registry
#	Keeps instances of chapters
class ChapterRegistry:
	
    def __init__(self):
    
        self.currentIndex = 0
        self.chapterList = []
    
    #   Adds a chapter to the list.
    def AddChapter(self, chapter):
        self.chapterList.append(chapter)
        
    #   Finds a chapter by name
    def FindChapterByName(self, chapterName):
    
        chapterToReturn = ""
       
        for chapter in self.chapterList:
            if chapter.chapterTitle == chapterName:
                chapterToReturn = chapter
        
        return chapterToReturn
                
    #   Increments the current index 
    def ProgressStory(self):
    
        self.currentIndex += 1
        
    #   Prints the story.
    def DisplayStory(self):
    
        while self.currentIndex != len(self.chapterList):
        
            cr = ChapterReader()
            r = Renderer()
            
            linesInFile = cr.ReadFile(self.chapterList[self.currentIndex].filePath)
            
            r.DisplayFullChapter(linesInFile, self.chapterList[self.currentIndex])
            
            userInput = input("PRESS ENTER TO PROGRESS")
            
            self.ProgressStory()
        
        