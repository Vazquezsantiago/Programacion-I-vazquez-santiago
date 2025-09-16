def mostrar(titulos, cantidad):
    for i in range(len(titulos)):
        print(f"{titulos[i]}->{cantidad[i]} ejemplares ")

def mostrar_agotados(titulos, cantidad):
    for i in range(len(titulos)):
        if cantidad[i] == 0:
            print(f"{titulos[i]} esta agotado")
salir=""
def agregar(titulos, cantidad,a):
    salir=""
    while a < 20 and salir != "x":
        
        nuevo = str(input("ingrese un nuevo titulo:"))
        stock = int(input("ingrese stock: "))
        titulos[a] = nuevo
        cantidad[a] = stock
        a+=1

        salir = input("ingrese x para salir")
def modificar(titulos, cantidad):
    for i in range(len(titulos)):
        a=int(input("ingrese que numero de titulo desea modificar"))
        c=int(input("ingrese el nuevo stock"))
        cantidad[a]=c
        print(f" el nuevo stock de{titulos[a]} es {cantidad[a]}")