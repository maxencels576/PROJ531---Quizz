from user import *
from quiz import *

def main():
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

        elif choix == "2":
            creer_quiz()

        elif choix == "3":
            print("\n--- Vos scores ---")
            if user[2] == "score0":
                print("Aucun score enregistré.")
            else:
                for s in user[2].split("|"):
                    if s != "score0":
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
        user[2] = user [2] + "-" + str(run_quiz(quiz))
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


if __name__ == "__main__":
    main()

