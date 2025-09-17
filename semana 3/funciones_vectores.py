
def buscar(array, numero):
    for i in range(len(array)):
        if numero == array[i]:
            print(f"{numero}esta en la posicion {array[i]}")
        else:
            print("-1")