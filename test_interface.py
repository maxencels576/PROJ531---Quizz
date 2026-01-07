from user import *
from quiz import *
from random import randint
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def clean():
    for widget in fenetre.winfo_children():
        widget.destroy()
        
users = load_user()
current_user = None

fenetre = Tk()
fenetre.title("Application Quiz")
fenetre.geometry("400x300")

def main():
    
    ecran_accueil()
    
    #Button(fenetre, text="1. Créer un compte", command = ecran_login())
    
    fenetre.mainloop()
    
    print("=== APPLICATION QUIZ ===")

    users = load_user()

    while True:
        print("\n--- Menu principal ---")
        print("1. Créer un compte")
        print("2. Se connecter")
        print("3. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            users.append(create_user(users))
            save_user(users)

        elif choix == "2":
            user = login(users)
            print(f"\nBienvenue {user[0]} !")
            menu_utilisateur(user, users)
            

        elif choix == "3":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")
        
        


def menu_utilisateur(user, users):
    while True:
        print("\n--- Menu utilisateur ---")
        print("1. Lancer un quiz")
        print("2. Créer un quiz")
        print("3. Voir mes scores")
        print("4. Se déconnecter")

        choix = input("Votre choix : ")

        if choix == "1":
            lancer_quiz(user)
            save_user(user)

        elif choix == "2":
            creer_quiz()

        elif choix == "3":
            print("\n--- Vos scores ---")
            if user[2] == "Scores : ":
                print("Aucun score enregistré.")
            else:
                for s in user[2].split("|"):
                    if s != "Scores : ":
                        print(s)

        elif choix == "4":
            save_user(users)
            print("Déconnexion...")
            break

        else:
            print("Choix invalide.")


def lancer_quiz(user):
    print("\n--- Liste des quiz disponibles ---")
    quizzes = list_quizzes_txt()

    if not quizzes:
        print("Aucun quiz disponible.")
        return

    for i, quiz_name in enumerate(quizzes):
        print(f"{i+1}. {quiz_name}")

    choix = input("Choisissez un quiz : ")

    try:
        choix = int(choix) - 1
        quiz_name = quizzes[choix]
    except:
        print("Choix invalide.")
        return

    quiz = load_quiz_txt(quiz_name)

    if quiz:
        user[2] = user[2] + quiz_name + " : " + str(run_quiz(quiz)) + "/" + str(len(quiz.questions)) + " - "
    else:
        print("Erreur lors du chargement du quiz.")

def creer_quiz():
    
    titre = input("Entrer un titre : ")

    nb_quest = int(input("Entrer le nombre de questions : "))
    nb_rep = int(input("Entrer le nombre de proposition par question : "))
    quiz = Quiz(titre)

    for i in range(nb_quest):

        question = input("Entrer la question n°" + str(i+1) + " : ")
        rep = []

        for j in range(nb_rep):
            rep.append(input("Entrer la proposition n°" + str(j+1) + " : "))

        sol = int(input("Entrer le numéro de la proposition correcte : ")) - 1
        quiz.add_question(Question(question,rep,sol))

    save_quiz_txt(quiz)

def ecran_accueil():
    label = Label(fenetre, text="Mintarra's Quizz", font=("Arial", 30), bg="turquoise")
    label1 = Label(fenetre, text="\n\n\nMenu principal\n", font=("Arial", 20))
    label2 = Label(fenetre, text="\n1. Créer un compte\n\n2. Se connecter\n\n3. Quitter")
    label.pack()
    label1.pack()
    label2.pack()
    # bouton
    
    

    # Label(fenetre, text="Identifiant").pack()
    # entry_user = Entry(fenetre)
    # entry_user.pack()

    # Label(fenetre, text="Mot de passe").pack()
    # entry_pass = Entry(fenetre, show="*")
    # entry_pass.pack()

def ecran_login():
    clean()

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
    # Button(fenetre, text="Quitter", command=fenetre.quit).pack()
    
if __name__ == "__main__":
    main()
    
