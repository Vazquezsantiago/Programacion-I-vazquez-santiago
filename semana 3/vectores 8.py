a = [0]*2
b = [0]*2
numero1 = 0
numero2 = 0
for i in range (len(a)):
    numero1 = int(input("ingrese un numero: "))
    a[i] = numero1

for i in range (len(b)):
    numero2 = int(input("ingrese un numero: " ))
    b[i] = numero2


print(a,b)


for i in range (len(a)):
    if numero1 == numero2:
        valor=True
    else:
        valor=False
if valor == True:
    print("son iguales")
else:
    print("no lo son")        
