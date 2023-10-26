class Person:
    name="Harpal"
    study="B.Tech"
    def info(self):
        print(f"{self.name} is Study in {self.study}")

a=Person()
a.name="Malay"
a.study="B.Tech"

b=Person()
b.name="Kinjal"
b.study="B.Com"

c=Person()
c.name="Purvi"
c.study="Nursing "

d=Person()

print(a.info())
print(b.info())
print(c.info())
print(d.info())

class Menu:
    branch="Samras Hostel"
    breakfast="Tea or Cofee"
    lunch="Dal Bhatt"
    dinner="Khichdi"
    def info(self):
        li=[]
        li.append(self.branch)
        li.append(self.breakfast)
        li.append(self.lunch)
        li.append(self.dinner)
        print("Menu: " , li)

g=Menu()    
g.branch="Gurukul"
g.breakfast="Pawa Batata"
g.lunch="Shak Rotli"
print(g.info())

r=Menu()
r.branch="RKU"
r.breakfast="Idali"
r.lunch="Dal shak roti sas"
r.dinner="Punjabi"
print(r.info())

s=Menu()
print(s.info())
