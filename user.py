class User():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.quiz_lst = []
        self.scores = []

def load_user():
    """
    Docstring for load_user
    recupere depuis un fichier txt un dictionnaire d'utilisateurs
    """
    #gestion d'un fichier texte
    with open('exemple.txt', 'a') as fichier:
        fichier.write("premiere ligne.\n")
        fichier.write("deuxième ligne.\n")

def save_user(users):
    """
    Docstring for save_user
    
    [[name1,password1,...],[name2,...]] ==> text 
    """
    with open('exemple.txt', 'w') as fichier:
        for user in users:
            for i in range(len(user)-1):
                fichier.write(str(user[i])+",")
            fichier.write(str(user[len(user)])+"\n")

def create_user(users):
    """
    Docstring for create_user
    renvoie un nouvel utilisateur 
    """
    username = input("donner un nom valide")
    password = input("donner un mot de passe valide")
    user = User(username, password)
    return user

def login(users):
    pass

    

        