cantidad_de_titulos=0

titulos= [0]*cantidad_de_titulos
ejemplares= [0]*cantidad_de_titulos
cantidad_de_titulos = int(input("ingrese cuantos titulos son: "))
while True:
    for i in range(cantidad_de_titulos):
        print("----menu de opciones----")
        t = str(input("ingresar titulo: "))
        e = int(input("ingrese cuantos ejemplares "))
        titulos[i]= t
        
        N=input(str("ingrese N para salir"))

        print(titulos)
    if N =="N":
            break
    