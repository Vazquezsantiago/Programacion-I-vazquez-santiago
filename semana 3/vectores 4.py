numero = [0]*8
suma =0
for a in range(len(numero)):
    a = int(input("ingrese un numero: "))
    if a > 100:
        suma += 1

print(f"usted ingreso {suma} numeros mayores a 100")
