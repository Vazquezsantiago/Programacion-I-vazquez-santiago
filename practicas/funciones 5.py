
def es_par(numero):
    if numero%2 == 0:
        return(numero,"es par")
    else:
        return(numero, "no es par")
num=int(input("ingrese un numero: "))

print(es_par(num))