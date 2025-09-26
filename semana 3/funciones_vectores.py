
def buscar(array, numero):
    for i in range(len(array)):
        if numero == array[i]:
            print(f"{numero}esta en la posicion {array[i]}")
        else:
            print("-1")


def ingresar(n_participantes, participantes):
    n_participantes = int(input("cuantos participantes desea ingresar?(max 10)"))
    for i in range(n_participantes):
        participantes[i]=str(input("ingrese el nombre del primer participantes:"))
        desea=str(input("desea agregar otro?(si/no)"))
        if desea== "no":
            break


