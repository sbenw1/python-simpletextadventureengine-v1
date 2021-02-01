
from os import system, name
from time import sleep

#	Attempts to clear a screen.
#   From "GEEKS FOR GEEKS"
def ClearScreen():

	os = ""
	
	#	For windows:
	if name == "nt":
		os = system("cls")
	
	#	For mac etc
	else:
		os = sysem("clear")

	