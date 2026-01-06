def load_user():
    """
    Docstring for load_user
    recupere depuis un fichier txt une liste d'utilisateurs
    """
    #gestion d'un fichier texte
    users = []
    with open('Comptes.txt', 'r') as fichier:
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
    with open('Comptes.txt', 'w') as fichier:
        for user in users:
            for ele in user:
                if ele != "" and ele != "\n" :
                    fichier.write(ele + ";")
            fichier.write("\n")

                
        

def create_user(users):
    """
    Docstring for create_user
    renvoie un nouvel utilisateur 
    """
    username = input("Donner un identifiant valide :\n")
    flag = True
    for user in users:
        if user[0] == username :
            flag = False
            
    while not flag :
        print("Cet identifiant existe déjà ! Veuillez réessayer")
        username = input("Donner un identifiant valide :\n")
        flag = True
        for user in users:
            if user[0] == username :
                flag = False
        
    password = input("Donner un mot de passe valide :\n")
    return [username,password,"Scores : "]

def login(users):
    username = input("Entrez votre identifiant :\n")
    for user in users:
        if user[0] == username:
            password = input("Entrez votre mot de passe :\n")
            while user[1] != password :
                print("Mot de passe invalide ! Veuillez réessayer")
                password = input("Entrez votre mot de passe :\n")
            if user[1] == password:
                return user
    print("Cet identifiant n'existe pas ! Veuillez réessayer\n")
    return login(users)
                

    

        