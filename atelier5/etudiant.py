class étudiant:
    def __init__(self,nom,prénom,age,moyenne):
        self.nom = nom
        self.prénom = prénom
        self.age = age
        self.moyenne = moyenne


    list = []
        # appending instances to list
    list.append(étudiant('Akash','aa', 2 , 12))
    list.append(étudiant('Deependra', 'bb' , 40 ,13))
    list.append(étudiant('Reaper', 'cc' , 44 , 14))

    for obj in list:
        print( obj.nom, obj.prénom, sep=' ' )

