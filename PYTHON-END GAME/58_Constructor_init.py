# class Person:
#     name="Harpal"
#     age=19
#     def work(self):
#         print(f"{self.name} is {self.age} years old")

# a=Person()
# a.name="Kinjal"
# a.age=18
# a.work()

# b=Person()
# b.name="Purvi"
# b.age=18
# b.work()

class Persons:
    name="Harpal"
    age=19
    def __init__(self,name,age):
        print("\nI am Object called by init")
        self.nm=name
        self.ag=age
        print(f"Hey! {self.nm} You are {self.ag} years old")

x=Persons("Kinjal",18)

y=Persons("Purvi",18)

z=Persons("Janak",22)
