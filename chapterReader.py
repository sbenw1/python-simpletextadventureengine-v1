
#   Chapter reader.
#   Reads each chapter .txt file
class ChapterReader:

    #   Reads a file.
    def ReadFile(self, fpath):
        linesInFile = [""]
        
        theFile = open(fpath, "r")
        
        for line in theFile:
            linesInFile.append(line)
        
        theFile.close()
        
        return linesInFile