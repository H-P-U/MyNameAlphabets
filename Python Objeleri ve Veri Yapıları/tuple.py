list=[1, 2, 3]
tuple=(1, 'iki', 3)

"""print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))"""
#listelerde karakter değişikliği yapılabilir ama tuple larda değişiklik yapılamaz
list=['Damla', 'Ayşe']
tuple=('Ali', 'Veli', 'Ayşe', 'Ayşe')
names=('Hatice', 'Pınar', 'Elif', 'Pelin')+ tuple
list[0]= 'Ahmet'
#tuple[0]= 'Ahmet'
print(list)
print(tuple.count('Ayşe'))
print(tuple.index('Ayşe'))
print(names)