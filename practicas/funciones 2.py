def operar(num1:int, num2:int):
    suma= num1 + num2
    resta= num1 - num2
    multiplicacion= num1 * num2
    return suma, resta, multiplicacion

numero=int(input("igrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))

print(operar(numero,numero2))
