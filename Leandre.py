from random import randint

class question():
    def __init__(self,quest,nb_rep,lst_rep,correction,point):
        self.quest = quest 
        self.nb_rep = nb_rep
        self.lst_rep = lst_rep
        self.correction = correction
        self.point = point

quest1 = "1+1 ?"
nb_rep1 = 3
lst_rep1 = ["1","2","3"]
c1 = 1
p1 = 1

quest2 = "1+2 ?"
nb_rep2 = 3
lst_rep2 = ["2","3","4"]
c2 = 1
p2 = 1

quest3 = "1+3 ?"
nb_rep3 = 3
lst_rep3 = ["3","4","5"]
c3 = 1
p3 = 1

q1 = question(quest1,nb_rep1,lst_rep1,c1,p1)

q2 = question(quest2,nb_rep2,lst_rep2,c2,p2)

q3 = question(quest3,nb_rep3,lst_rep3,c3,p3)

def quizz(nb_question,lst_quest):
    score = 0
    qused = []
    for i in range(nb_question):
        r = randint(0,len(lst_quest)-1)
        while lst_quest[r] in qused:
            r = randint(0,len(lst_quest)-1)
        randq = lst_quest[r]

        qused.append(randq)

        print(randq.quest)
        for rep in randq.lst_rep:
            print(rep)
        print("quelle est votre réponse ?")

        if int(input("entrez le numéro de la proposition "))-1 == randq.correction:
            print("bravo ! C'était la bonne réponse")
            score += 1
        else:
            print("oh non la bonne réponse était " + randq.lst_rep[randq.correction])
    
    
    print("tu as un score de : " + str(score))
        

quizz(3,[q1,q2,q3])
        


