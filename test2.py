from tkinter import *
from tkinter.messagebox import showinfo, showerror

# IMPORTS DE TES PROGRAMMES
from user import * # load_user, save_user
from quiz import * # load_quiz_txt, list_quizzes_txt
from quiz import * # run_quiz   # la fonction Tkinter créée avant


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
    label = Label(fenetre, text="\n\n\n").pack()

    Button(fenetre, text="J'ai déjà un compte", command=ecran_login).pack()
    label = Label(fenetre, text="\n").pack()
    Button(fenetre, text="Je suis un nouvel utilisateur", command=ecran_create).pack()
    label = Label(fenetre, text="\n").pack()
    Button(fenetre, text="Quitter", command=fenetre.destroy).pack()

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
        users.append([username, password, ""])
        save_user(users)

        showinfo("Succès", "Compte créé avec succès")
        ecran_login()

    Button(fenetre, text="Créer", command=creer).pack(pady=10)
    Button(fenetre, text="Retour", command=ecran_begining).pack()
    Button(fenetre, text="Quitter", command=fenetre.destroy).pack()

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

# Création d'un Quiz
def ecran_create_quiz():
    clear()
    
    Label(fenetre, text="Bienvenue dans le menu pour la création de quiz", font=("Arial", 14)).pack(pady=10)
    
    Label(fenetre, text="Quel nom voulez-vous donner à votre quiz ?").pack()
    entry_title = Entry(fenetre)
    entry_title.pack()
    
    Label(fenetre, text="Combien de questions voulez-vous ?").pack()
    entry_nbq = Entry(fenetre)
    entry_nbq.pack()

    Label(fenetre, text="Combien de propositions voulez-vous mettre par question ?").pack()
    entry_nbp = Entry(fenetre)
    entry_nbp.pack()
    
    quiz = Quiz(entry_title)


# Menu utilisateur
def ecran_menu():
    clear()

    Label(fenetre, text=f"Bienvenue {current_user[0]}", font=("Arial", 14)).pack(pady=10)

    Button(fenetre, text="Lancer un quiz", command=ecran_quiz).pack(pady=5)
    Button(fenetre, text="Créer un quiz", command=ecran_create_quiz).pack(pady=5)
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

    if current_user[2] == "":
        Label(fenetre, text="Aucun score").pack()
    else:
        for s in current_user[2].split("-"):
            if s.strip():
                Label(fenetre, text=s + "\n").pack(anchor="w", padx=20)

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
