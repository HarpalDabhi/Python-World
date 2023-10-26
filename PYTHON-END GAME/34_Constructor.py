class Play:
    def __init__(self,name,score,game):
        self.n = name
        self.s=score
        self.g=game
        print(f"{self.n} has scored {self.s} in the {self.g} \n")

a=Play("Harpal",98,"Chess")

b=Play("Hiten",100,"PubG")

c=Play("Vija",100,"FreeFire")

class War:
    def __init__(self,killer,killed,day,weapon):
        self.killer = killer
        self.killed = killed
        self.day = day
        self.weapon = weapon
        print(f"{self.killer} has killed {self.killed} on {self.day}'s day in Mahabhrat by using his {self.weapon} weapon.\n")

a=War("Arjun","Karna",17,"Arrow")

b=War("Bheem","Duryodhan",18,"Mace")

c=War("Sikhandi","Bhisma",10,"Arrow")

d=War("All","Abhimanyu",11,"All type")


