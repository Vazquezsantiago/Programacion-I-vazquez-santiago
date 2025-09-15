numero = [0]*7
mayor=0
for i in range (len(numero)):
        valor=int(input("inserte un numero: "))
        numero[i] = valor
        if valor > mayor:
                mayor = valor


print(f"el valor mas alto es {mayor} y se encuentra en {numero[i]}")
