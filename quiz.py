import os

class Question:
    """
    quest (str) : texte de la question
    choix (list[str]) : choix disponibles
    rep (int) : index de la bonne réponse
    """

    def __init__(self, quest, choix, rep):
        self.quest = quest
        self.choix = choix
        self.rep = rep



class Quiz:
    """
    name (str) : nom du quiz
    questions (list[Question]) : liste des questions
    """

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        if not isinstance(question, Question):
            raise TypeError("add_question attend un objet Question")
        self.questions.append(question)



def save_quiz_txt(quiz):
    """
    Sauvegarde un quiz au format TXT.
    Format :
        QUESTION: ...
        CHOIX: a | b | c
        REP: index
    """

    filename = f"{quiz.name}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"QUIZ: {quiz.name}\n\n")

        for q in quiz.questions:
            f.write(f"QUESTION: {q.quest}\n")
            f.write("CHOIX: " + " | ".join(q.choix) + "\n")
            f.write(f"REP: {q.rep}\n\n")

    print(f"[OK] Quiz '{quiz.name}' sauvegardé en TXT.")


def load_quiz_txt(name):
    """
    Charge un quiz .txt et renvoie un objet Quiz.
    """

    filename = f"{name}.txt"

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le quiz '{name}.txt' n'existe pas.")

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    quiz = Quiz(name)

    quest = None
    choix = None
    rep = None

    for line in lines:
        line = line.strip()

        if line.startswith("QUESTION:"):
            quest = line[len("QUESTION:"):].strip()

        elif line.startswith("CHOIX:"):
            raw = line[len("CHOIX:"):].strip()
            choix = [c.strip() for c in raw.split("|")]

        elif line.startswith("REP:"):
            rep = int(line[len("REP:"):].strip())
            quiz.add_question(Question(quest, choix, rep))

    return quiz


def list_quizzes_txt():
    """
    Liste tous les quiz disponibles dans notre dossier
    """
    quizzes = []
    
    for f in os.listdir():
        if f.endswith(".txt"):
            quizzes.append(f[:-4])  # enlève .txt

    return quizzes



def run_quiz(quiz):
    """
    Exécute un quiz question par question
    et renvoie le score final.
    """

    print(f"\n=== Quiz : {quiz.name} ===\n")

    score = 0

    for i, question in enumerate(quiz.questions):
        print(f"Question {i+1}/{len(quiz.questions)}")
        print(question.quest)

        # Affichage des choix
        for idx, choice in enumerate(question.choix):
            print(f"  {idx}. {choice}")

        # Lecture sécurisée
        while True:
            try:
                user = int(input("Votre réponse : "))
                if 0 <= user < len(question.choix):
                    break
                else:
                    print("Indice invalide.")
            except ValueError:
                print("Veuillez entrer un nombre.")

        # Vérification
        if user == question.rep:
            score += 1
            print("✔ Bonne réponse !\n")
        else:
            print(f"✘ Mauvaise réponse. Bonne réponse : {question.rep}\n")

    print(f"=== Score final : {score}/{len(quiz.questions)} ===\n")
    return score