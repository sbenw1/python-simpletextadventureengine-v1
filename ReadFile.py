
#	This file reads text files.

def ReadFile(fpath):

    linesInFile = [""]
	
    theFile = open(fpath, "r")
	
    for line in theFile:
        linesInFile.append(line)
	
    theFile.close()
    
    return linesInFile