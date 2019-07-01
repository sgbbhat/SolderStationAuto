from tkinter import *
from tkinter import filedialog

def browse_button():
	global folder_path
	filename = filedialog.askdirectory()
	folder_path.set(filename)
	print(filename)

root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root, textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text= "Browse", command=browse_button)
button2.grid(row=0, column=3)

root.geometry("550x550+10+10")
root.mainloop()

