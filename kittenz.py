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
	files.geometry("0x185")
	scrollbar = Scrollbar(files)
	scrollbar.pack( side = RIGHT, fill = Y )
	txt_files = glob.glob(dir_path+"\\"+"*.txt")

	mylist = Listbox(files, height=10, width=16, yscrollcommand=scrollbar.set)

	for x in range(0, len(txt_files)):
		splited = txt_files[x].split("\\")
		txt = splited[-1]
		mylist.insert(END, txt)

	mylist.place(x=0, y=0)
	scrollbar.config(command=mylist.yview)

	def openFile():
		insert_index=0
		selection = mylist.curselection()
		index = selection[0]
		file = open(txt_files[index], "r")
		text.insert(1.0, file.read())
		splited = txt_files[x].split("\\")
		splited = splited[-1].split(".")
		name = splited[0]
		entry.insert(1, name)

	def deleteFile():
		selection = mylist.curselection()
		index = selection[0]
		os.remove(txt_files[index])
		mylist.selection_clear(index)
		mylist.delete(index)

	buttonOpen = Button(files, text="open", command=openFile)
	buttonOpen.place(x=50, y=162.5, height=25, width=50)
	buttonDelete = Button(files, text="delete", command=deleteFile)
	buttonDelete.place(x=0, y=162.5, height=25, width=50)

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.config(cursor="clock red red")
fenetre.title('Text editor by Gwen, Laurinnnnne et Nico')
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
