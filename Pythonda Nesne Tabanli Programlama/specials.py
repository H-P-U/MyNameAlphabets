myList=[1, 2, 3]
"""myString= 'my string'

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))"""

class Movie():
    def __init__(self, title, director, duration):
        self.title= title
        self.director=director
        self.duration=duration
        print('Movie objesi oluşturuldu.')
    def __str__(self):
        return f"{self.title} by {self.director}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print('Movie deleted.')

m=Movie('film adı', 'yönetmen adı', 120)

#print(len(myList))
#print(len(m))
print(str(m))

'''del m
print(m)'''