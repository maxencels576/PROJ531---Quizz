class Question():
    def __init__(self,quest,lst_rep,correction):
        self.quest = quest 
        self.lst_rep = lst_rep
        self.correction = correction



class Quiz():
    def __init__(self,name):
        self.name = name
        self.question = []
        

quest1 = "1+1 ?"
lst_rep1 = ["1","2","3"]
c1 = 1
p1 = 1

quest2 = "1+2 ?"
lst_rep2 = ["2","3","4"]
c2 = 1
p2 = 1

quest3 = "1+3 ?"
lst_rep3 = ["3","4","5"]
c3 = 1
p3 = 1

q1 = Question(quest1,lst_rep1,c1,p1)

q2 = Question(quest2,lst_rep2,c2,p2)

q3 = Question(quest3,lst_rep3,c3,p3)