class Val:
    x=10
    y=15
v1=Val()
print(v1.y)

class Person1:
    name="Harpal"
    std=3

p1=Person1()
print(p1.name)

class Person2:
    def  __init__(self, name,std):
        self.name=name
        self.std=std

p2=Person2("H",3)
print(p2.name)


class Mahabhrat:
    def __init__(self,name,skill):
        self.nm=name
        self.skl=skill
        print(f"{self.nm} has {self.skl} skill ")

m1=Mahabhrat("Arjun","Archery")

m1=Mahabhrat("Bheem","MaceWar")

class Best_friend:
    def __init__(self,fr1,fr2):
        self.fr1=fr1
        self.fr2=fr2
        print(f" 🫥 {fr2} and {fr1} are Best Friends Forever 🫥 \n\b\b**********************\n")

f1=Best_friend("Harpal","Vishal")

f2=Best_friend("Karna","Duryodhan")

f3=Best_friend("Harpal","Vipul")

f4=Best_friend("Malay","Elesh")

f5=Best_friend("Krishna","Sudama")

import mymodule

print(mymodule.a)