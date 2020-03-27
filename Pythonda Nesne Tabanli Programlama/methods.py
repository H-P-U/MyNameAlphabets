"""#class

class Person:
    # pass #yer tutar, kodun hata vermeden devamını sağlar
    #class attributes
    adress='no information'
    #constructur
    def __init__(self,name,year):
        #object attributes
        self.name= name
        self.year= year
    #instance methods
    def intro(self):
        print('Hello There. I am'+ self.name )
    # instance methods
    def calculateAge(self):
        return 2020-self.year

#object,instance
p1= Person(name='Pınar', year=1995)
p2=Person(name='Zehra',year=1993)

p1.intro()
p2.intro()


print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')"""

class Circle:
    #Class object attribute
    pi=3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    #Methods
    def CevreHesapla(self):
        return 2*self.pi*self.yaricap
    def AlanHesapla(self):
        return self.pi*(self.yaricap**2)


c1=Circle() #yaricap=1 alır
c2= Circle(5)

print(f'c1 Alan: {c1.AlanHesapla()} , c1 Çevre: {c1.CevreHesapla()}')
print(f'c2 Alan: {c2.AlanHesapla()} , c2 Çevre: {c2.CevreHesapla()}')