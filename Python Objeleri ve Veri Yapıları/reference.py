#Value Type => string, number => value type larla listenin kendisiyle ilgileniyoruz
x=25
y=5

x=y
y=10 #bu değişiklik x i etkilemez

#print(x,y)

#reference types => list, class => reference type larda listenin adresiyle ilgileniyoruz

a=['apple','banana']
b=['apple','banana']

a=b
b[0]= 'grape' #reference yapılan değişiklik a yı da etkiledi

print(a,b)
