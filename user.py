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
    with open('main.txt', 'r') as fichier:
        return fichier.readlines()

def save_user(users):
    """
    Docstring for save_user
    
    [[name1,password1,...],[name2,...]] ==> text 
    """
    with open('main.txt', 'w') as fichier:
        print(users)
        for user in users:
            print(user)
            fichier.write(str(user))
            fichier.write("\n")
        

def create_user(users):
    """
    Docstring for create_user
    renvoie un nouvel utilisateur 
    """
    username = input("Donner un nom valide :\n")
    password = input("Donner un mot de passe valide :\n")
    user = username
    #user = User(username, password)
    return user

def login(users):
    username = input("Donner un nom valide :\n")
    #if username in users:
        #password = input("Donner un mot de passe valide :\n")
            #if username[password] == password:
    return username

    

        