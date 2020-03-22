for x in range(10):
    print(x)
numbers =[x for x in range(10)]
print(numbers)

numbers= [x*x for x in range(10) if x%3==0]
print(numbers)

myString='Hello'
myList=[]

for letter in myString:
    myList.append(letter)
print(myList)

myList= [letter for letter in myString]
print(myList)

years=[1995, 1998, 2010, 1956,1980]
ages=[2020-year for year in years]
print(ages)

results=[x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)

result=[]

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers=[ (x,y)  for x in range(3) for y in range(3)]
print(numbers)
