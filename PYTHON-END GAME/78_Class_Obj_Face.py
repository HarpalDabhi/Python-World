g_li=["Manisha","Divya","Deev","Mansi","Prerna"]
b_li=["Harpal","Vipul","Aditya","Jeel","Malay"]

class Facebook:
    y_name="Divya"
    m_name="Harpal"
    def connection(self):
        if self.y_name in g_li:
            print("You have Girl Now !!! 🥰🥰🥰")
            ans=input("Do you want to be friend ??")
            if ans=="y":
                print("You are Friends right Now !!! ❤️❤️❤️")
            else:
                print("You are Connected !!! 🛞🛞🛞")
        elif self.m_name in b_li:
            print("You have Boy Now 🥶🥶🥶")
        else:
            print("😩😩😩")


a=Facebook()
a.y_name="Aditi"
a.m_name="Harsh"
# a.connection()

b=Facebook()
b.y_name="Manisha"
b.m_name="Malay"
# b.connection()

class Bank:
    print("You Visited Bank")
    branch="BOB"
    account=8498100003272
    def details(self):
        print(f"Branch -- > {self.branch}")
        print(f"Account No. -- > {self.account}")
        print("____________\n")

c=Bank()
c.branch="SBI"
c.account=98789794164546
c.details()
