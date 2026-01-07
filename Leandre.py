from random import randint
from tkinter import *
"""
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























"""
#gestion d'un fichier texte
with open('exemple.txt', 'a') as fichier:
    fichier.write("premiere ligne.\n")
    fichier.write("deuxième ligne.\n")
"""










"""
#fonctionnement tkinter

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
def afficher_selection():
    selection = liste.get(liste.curselection())# Récupère l'élément sélectionné
    print("Élément sélectionné :", selection)


bouton=Button(fenetre, text="affiche", command=afficher_selection)
bouton.pack()



fenetre.mainloop()

"""

"""

#get() permet de récupérer la valeur associée à cet indice.

import tkinter as tk
# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple de Listbox")
# Création d'une Listbox
liste = tk.Listbox(root)
liste.pack()
# Création d'une liste d'éléments à ajouter
elements = ["Python", "Java", "C++", "JavaScript"]
# Ajout des éléments à la Listbox
for element in elements:
    liste.insert(tk.END, element)
def afficher_selection():
    selection = liste.get(liste.curselection())# Récupère l'élément sélectionné
    print("Élément sélectionné :", selection)
# Création d'un bouton pour afficher la sélection
btn_afficher = tk.Button(root,text="Afficher sélection",command=afficher_selection)
btn_afficher.pack()
root.mainloop()
"""


from tkinter import *
from tkinter.messagebox import showinfo, showerror

# IMPORTS DE TES PROGRAMMES
from user import load_user, save_user
from quiz import load_quiz_txt, list_quizzes_txt
from quiz import run_quiz   # la fonction Tkinter créée avant


# Variables globales

users = load_user()
current_user = None


# Fenêtre principale

fenetre = Tk()
fenetre.title("Application Quiz")
fenetre.geometry("400x300")


# ÉCRANS

def clear():
    for widget in fenetre.winfo_children():
        widget.destroy()

# Ecran d'accueil
def ecran_begining():
    clear()
    label = Label(fenetre, text="\n").pack()
    label = Label(fenetre, text="Mintarra's Quizz", font=("Arial", 30), bg="turquoise").pack()
    label = Label(fenetre, text="\n").pack()

    Button(fenetre, text="J'ai déjà un compte", command=ecran_login).pack()
    Button(fenetre, text="Je suis un nouvel utilisateur", command=ecran_create).pack()


# Ecran création de compte
def ecran_create():
    clear()

    Label(fenetre, text="Créer un compte", font=("Arial", 14)).pack(pady=10)

    Label(fenetre, text="Identifiant").pack()
    entry_user = Entry(fenetre)
    entry_user.pack()

    Label(fenetre, text="Mot de passe").pack()
    entry_pass = Entry(fenetre, show="*")
    entry_pass.pack()

    def creer():
        username = entry_user.get().strip()
        password = entry_pass.get().strip()

        if not username or not password:
            showerror("Erreur", "Champs obligatoires")
            return

        # Vérifier si l'utilisateur existe déjà
        for user in users:
            if user[0] == username:
                showerror("Erreur", "Identifiant déjà utilisé")
                return

        # Créer l'utilisateur
        users.append([username, password, "Scores : "])
        save_user(users)

        showinfo("Succès", "Compte créé avec succès")
        ecran_login()

    Button(fenetre, text="Créer", command=creer).pack(pady=10)
    Button(fenetre, text="Retour", command=ecran_begining).pack()


# Écran connexion
def ecran_login():
    clear()

    Label(fenetre, text="Connexion", font=("Arial", 14)).pack(pady=10)

    Label(fenetre, text="Identifiant").pack()
    entry_user = Entry(fenetre)
    entry_user.pack()

    Label(fenetre, text="Mot de passe").pack()
    entry_pass = Entry(fenetre, show="*")
    entry_pass.pack()

    def connexion():
        global current_user

        username = entry_user.get()
        password = entry_pass.get()

        for user in users:
            if user[0] == username and user[1] == password:
                current_user = user
                ecran_menu()
                return

        showerror("Erreur", "Identifiant ou mot de passe incorrect")

    Button(fenetre, text="Se connecter", command=connexion).pack(pady=10)
    Button(fenetre, text="Retour", command=ecran_begining).pack()
    Button(fenetre, text="Quitter", command=fenetre.destroy).pack()


# Menu utilisateur
def ecran_menu():
    clear()

    Label(
        fenetre,
        text=f"Bienvenue {current_user[0]}",
        font=("Arial", 14)
    ).pack(pady=10)

    Button(fenetre, text="Lancer un quiz", command=ecran_quiz).pack(pady=5)
    Button(fenetre, text="Voir mes scores", command=voir_scores).pack(pady=5)
    Button(fenetre, text="Déconnexion", command=logout).pack(pady=5)


# Liste des quiz
def ecran_quiz():
    clear()

    Label(fenetre, text="Choisir un quiz", font=("Arial", 14)).pack(pady=10)

    quizzes = list_quizzes_txt()

    liste = Listbox(fenetre)
    for q in quizzes:
        liste.insert(END, q)
    liste.pack()

    def lancer():
        selection = liste.curselection()
        if not selection:
            showerror("Erreur", "Sélectionnez un quiz")
            return

        nom = quizzes[selection[0]]
        quiz = load_quiz_txt(nom)

        score = run_quiz(quiz)

        current_user[2] += f"{nom} : {score}/{len(quiz.questions)} | "
        save_user(users)

        ecran_menu()

    Button(fenetre, text="Lancer", command=lancer).pack(pady=10)
    Button(fenetre, text="Retour", command=ecran_menu).pack()


# Scores
def voir_scores():
    clear()

    Label(fenetre, text="Mes scores", font=("Arial", 14)).pack(pady=10)

    if current_user[2] == "Scores : ":
        Label(fenetre, text="Aucun score").pack()
    else:
        for s in current_user[2].split("|"):
            if s.strip():
                Label(fenetre, text=s).pack(anchor="w", padx=20)

    Button(fenetre, text="Retour", command=ecran_menu).pack(pady=10)

# -----------------------
def logout():
    global current_user
    current_user = None
    save_user(users)
    ecran_login()

# -----------------------
ecran_begining()
fenetre.mainloop()
