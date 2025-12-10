def load_user():
    """
    Docstring for load_user
    recupere depuis un fichier txt une liste d'utilisateurs
    """
    #gestion d'un fichier texte
    users = []
    with open('main.txt', 'r') as fichier:
        f_users = fichier.readlines()
        for user in f_users:
            ele = user.split(";")
            users.append(ele)
    return users



def save_user(users):
    """
    Docstring for save_user
    
    [[name1,password1,...],[name2,...]] ==> text 
    """
    with open('main.txt', 'w') as fichier:
        for user in users:
            for ele in user:
                fichier.write(ele+";")
            fichier.write("\n")

                
        

def create_user(users):
    """
    Docstring for create_user
    renvoie un nouvel utilisateur 
    """
    username = input("Donner un identifiant valide :\n")
    password = input("Donner un mot de passe valide :\n")
    return [username,password,"score0"]

def login(users):
    username = input("Entrez votre identifiant :\n")
    for user in users:
        if user[0] == username:
            password = input("Entrez votre mot de passe :\n")
            if user[1] == password:
                return user

    

        