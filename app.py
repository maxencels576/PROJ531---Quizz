from user import load_users, save_users, create_user, login
from quiz import load_quiz_txt, list_quizzes_txt, run_quiz

def main():
    print("=== APPLICATION QUIZ ===")

    users = load_users()

    while True:
        print("\n--- Menu principal ---")
        print("1. Créer un compte")
        print("2. Se connecter")
        print("3. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            create_user(users)
            save_users(users)

        elif choix == "2":
            user = login(users)
            if user:
                print(f"\nBienvenue {user.username} !")
                menu_utilisateur(user, users)

        elif choix == "3":
            print("Au revoir !")
            save_users(users)
            break

        else:
            print("Choix invalide.")


def menu_utilisateur(user, users):
    while True:
        print("\n--- Menu utilisateur ---")
        print("1. Lancer un quiz")
        print("2. Voir mes scores")
        print("3. Se déconnecter")

        choix = input("Votre choix : ")

        if choix == "1":
            lancer_quiz(user)

        elif choix == "2":
            print("\n--- Vos scores ---")
            if not user.scores:
                print("Aucun score enregistré.")
            else:
                for s in user.scores:
                    print(f"{s['quiz']} : {s['score']} / {s['total']}")

        elif choix == "3":
            save_users(users)
            print("Déconnexion...")
            break

        else:
            print("Choix invalide.")


def lancer_quiz(user):
    print("\n--- Liste des quiz disponibles ---")
    quizzes = list_quizzes()

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

    quiz = load_quiz(quiz_name)

    if quiz:
        play_quiz(quiz, user)
    else:
        print("Erreur lors du chargement du quiz.")


if __name__ == "__main__":
    main()
