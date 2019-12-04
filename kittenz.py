#!usr/bin/python
from tkinter import *
from PIL import Image
import glob
import os
import matplotlib.pyplot as plt
from functools import partial

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def retrieve():
	retrieve_text = text.get("1.0", "end-1c")
	retrieve_entry = entry.get()

	file = open(dir_path+"\\"+retrieve_entry+".txt", "w")
	file.write(retrieve_text)

def file_manager():
	files = Tk()
	files.title("files")
	files.geometry("400x200")
	scrollbar = Scrollbar(files)
	scrollbar.pack( side = RIGHT, fill = Y )
	txt_files = glob.glob(dir_path+"\\"+"*.txt")
	txt_buttons = glob.glob(dir_path+"\\"+"*.txt")
	y = 25

	def open_file(index):
		test = open(txt_files[index])
		for char in test:
			print(char)

	mylist = Listbox(files, width=20, height=2, yscrollcommand = scrollbar.set )

	for x in range(0, len(txt_files)):
		splited = txt_files[x].split("\\")
		txt = splited[-1]
		mylist.insert(END, txt)

		# txt_buttons[x] = Button(files, text=txt, command=partial(open_file, x))
		# txt_buttons[x].place(x=75, y=y, width=300, height=25)
		# y += 35
	mylist.pack(side=LEFT, fill=BOTH)
	scrollbar.config(command=mylist.yview)

	def openFile():
		selection = mylist.curselection()
		index = selection[0]
		print(txt_files[index])

	def deleteFile():
		selection = mylist.curselection()
		index = selection[0]
		os.remove(txt_files[index])
		print(index)
		mylist.delete(index)
		mylist.selection_clear(index)

	buttonOpen = Button(files, text="open", command=openFile)
	buttonOpen.place(x=200, y=100, height=25, width=50)
	buttonDelete = Button(files, text="delete", command=deleteFile)
	buttonDelete.place(x=250, y=100, height=25, width=50)

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.config(cursor="clock red red")
fenetre.title('save it as .txt you retard')
fenetre.geometry('650x650')
fenetre.resizable(width=False, height=False)

#zone de texte
text = Text(fenetre)
text.place(x=75, y=75, width=500, height=500)

load_file = Button(fenetre, text="manage file", command=file_manager)
load_file.place(x=75, y=20, width=117.5, height=25)

contenu = Button(fenetre, text="save", command=retrieve)
contenu.place(x=202.5, y=20, width=117.5, height=25)

label = Label(fenetre, text="save: ")
label.place(x=330, y=20, width=30, height=25)

entry = Entry(fenetre)
entry.place(x=370, y=20, width=205, height=25)

#le bouton quitter
quit = Button(fenetre, text="FUCK OFF", fg="black")
quit.config(command=fenetre.destroy)
quit.pack(side = BOTTOM)


# On lance tout le bordel
fenetre.mainloop()
