a = [0]*10

for i in range (len(a)):
    numero1 = int(input("ingrese un numero: "))
    if numero1 %2 == 0:
        numero1=0
        a[i] = numero1
    a[i] = numero1

for i in range(len(a)):
    print(a[i])