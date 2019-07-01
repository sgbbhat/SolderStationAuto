from tkinter import filedialog
from tkinter import *
from tkinter import messagebox 

# Create a lable with passed parameters and place them in a location mentioned

def CreateLabel(root, Lname, Ltext , Lheight,  Lwidth, Lrelief, Lbg, Lfg, Lfont, Lplacex, Lplacey):
	Lname = Label(root, text = Ltext , height = Lheight,  width = Lwidth, relief = Lrelief, bg=Lbg, fg=Lfg, font = Lfont, anchor = 'w')
	Lname.place(x=Lplacex, y=Lplacey)
	return Lname
