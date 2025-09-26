
def buscar(array, numero):
    for i in range(len(array)):
        if numero == array[i]:
            print(f"{numero}esta en la posicion {array[i]}")
        else:
            print("-1")


def ingresar(n_participantes, participantes,puntuacion):
    n_participantes = int(input("cuantos participantes desea ingresar?(max 10)"))
    for i in range(n_participantes):
        nombre=str(input(f"ingrese el nombre del  participante {i+1}:"))
        nota=int(input(f"ingrese la puntuacion del participante {i+1}"))
        participantes[i]=nombre
        puntuacion[i]=nota

        desea=str(input("desea agregar otro?(si/no)"))
        if desea== "no":
            break

def mostrar(participantes,nota):
    for i in range (len(participantes)):
        print(participantes)
        print(nota)
    
