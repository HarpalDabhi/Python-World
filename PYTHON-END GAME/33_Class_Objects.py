class Love:
    pati="Krishna"
    patni="Radha"
    def prem(self):
        print(f"{self.pati} loves {self.patni}  a Lot.")

a=Love()
a.pati="Duryodhan"
a.patni="Bhanumati"
print(a.prem())

b=Love()
b.pati="Arjun"
b.patni="Subhadra"
print(b.prem())

c=Love()
c.pati="Bheem"
c.patni="Hidimba"
print(c.prem())

d=Love()
d.patni="Satyabhama"
print(d.prem())

e=Love()
e.pati="harpal"
print(e.prem())

f=Love()
f.pati="Bhisma"
f.patni=None
print(f.prem())

g=Love()
g.pati="Shantanu"
g.patni=['A', 'B', 'c']
print(g.prem())

