#class

class Person:
   # pass #yer tutar, kodun hata vermeden devamını sağlar
    #class attributes
    adress='no information'

    #constructur

    def __init__(self,name,year):
        #object attributes
        self.name= name
        self.year= year


    #methods

#object,instance
p1= Person('Pınar',1995)
p2=Person('Zehra',1993)

print(f'name: {p1.name} , year: {p1.year} , adress: {p1.adress}' )
print(f'name: {p2.name} , year: {p2.year}, adress: {p2.adress}')

