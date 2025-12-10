from user import *
from quiz import *

def main():
    print("=== Application Quiz ===")
    
    users = load_users()

    while True:
        print("")
        print("")
        print("")

        choix = input("")

        if choix == "1":
            users.append(create_user())
        elif choix == "2":
            user = login(users)
        else :
            break
    
    save_users(users)





            