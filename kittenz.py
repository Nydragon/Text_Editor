#!usr/bin/python
from tkinter import *
from PIL import Image
import glob
#import numpy as np
import matplotlib.pyplot as plt

def retrieve():
	print(text.get("1.0", "end-1c"))
	retrieve_text = text.get("1.0", "end-1c")
	retrieve_entry = entry.get()

	file = open(retrieve_entry+".txt", "w")
	file.write(retrieve_text)

def file_manager():
	files = Tk()
	files.title("files")
	files.geometry("450x650")
	txt_files = glob.glob("*.txt")
	txt_buttons = glob.glob("*.txt")
	print(txt_buttons)
	y = 25

	def open_file(index):
		test = open(txt_files[index])
		for char in test:
			print(char)

	for x in range(0, len(txt_files)):
		txt_buttons[x] = Button(files, text="open "+txt_files[x], command=open_file(x))
		txt_buttons[x].place(x=75, y=y, width=300, height=25)
		y += 35



# On crée une fenêtre, racine de notre interface
fenetre = Tk()
fenetre.config(cursor="clock red red")
fenetre.title('save it as .txt you retard')
fenetre.geometry('650x650')
fenetre.resizable(width=False, height=False)

#zone de texte
text = Text(fenetre)
text.place(x=75, y=75, width=500, height=500)

# #on tente une image wesh, on veut un FUCKING CHATON TROP MIGNON
# imgpil = Image.open("kitten.png")
# # anciennement np.asarray
# img = np.array(imgpil) # Transformation de l'image en tableau numpy
# plt.imshow(img)
# plt.show()

#couleur du texte
var_choix = StringVar()

# Déclarer les boutons
# choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="Rouge")
# choix_rouge.place(x=130, y=20, width=75, height=25)
# choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="Vert")
# choix_vert.place(x=200, y=20, width=75, height=25)
# choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="Bleu")
# choix_bleu.place(x=280, y=20, width=75, height=25)

# permet de récupérer les données d'une entrée
var_choix.get()

load_file = Button(fenetre, text="open file", command=file_manager)
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
