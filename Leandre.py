from random import randint
from tkinter import *

class question():
    def __init__(self,quest,nb_rep,lst_rep,correction):
        self.quest = quest 
        self.nb_rep = nb_rep
        self.lst_rep = lst_rep
        self.correction = correction

quest1 = "1+1 ?"
nb_rep1 = 3
lst_rep1 = ["1","2","3"]
c1 = 1
p1 = 1

quest2 = "1+2 ?"
nb_rep2 = 3
lst_rep2 = ["2","3","4"]
c2 = 1
p2 = 1

quest3 = "1+3 ?"
nb_rep3 = 3
lst_rep3 = ["3","4","5"]
c3 = 1
p3 = 1

q1 = question(quest1,nb_rep1,lst_rep1,c1,p1)

q2 = question(quest2,nb_rep2,lst_rep2,c2,p2)

q3 = question(quest3,nb_rep3,lst_rep3,c3,p3)

def quizz(nb_question,lst_quest):
    score = 0
    qused = []
    for i in range(nb_question):
        r = randint(0,len(lst_quest)-1)
        while lst_quest[r] in qused:
            r = randint(0,len(lst_quest)-1)
        randq = lst_quest[r]

        qused.append(randq)

        print(randq.quest)
        for rep in randq.lst_rep:
            print(rep)
        print("quelle est votre réponse ?")

        if int(input("entrez le numéro de la proposition "))-1 == randq.correction:
            print("bravo ! C'était la bonne réponse")
            score += 1
        else:
            print("oh non la bonne réponse était " + randq.lst_rep[randq.correction])
    
    
    print("tu as un score de : " + str(score))
        

#quizz(3,[q1,q2,q3])
        

























"""
#gestion d'un fichier texte
with open('exemple.txt', 'a') as fichier:
    fichier.write("premiere ligne.\n")
    fichier.write("deuxième ligne.\n")
"""









"""

fonctionnement tkinter

fenetre = Tk()

# label
label = Label(fenetre, text="Texte par défaut", bg="yellow")
label.pack()

# entrée
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack()

# checkbutton
bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()

# radiobutton
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

# canvas
canvas = Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

# scale
value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()

fenetre['bg']='white'

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


fenetre.mainloop()
"""
