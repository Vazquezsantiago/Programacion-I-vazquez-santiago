from funciones_vectores import *
cantidad_de_titulos=0
cantidad_de_titulos = int(input("ingrese cuantos titulos son: "))
titulos= [0]*cantidad_de_titulos
ejemplares= [0]*cantidad_de_titulos

N=""
while cantidad_de_titulos <= 20:
        for i in range(len(titulos)):
            print("----menu de opciones----")
            t = str(input("ingresar titulo: "))
            e = int(input("ingrese cuantos ejemplares "))
            titulos[i]= t
            ejemplares[i]= e
            cantidad_de_titulos +=1
            N=input(str("ingrese N para salir"))
        mostrar(titulos,ejemplares)
        mostrar_agotados(titulos, ejemplares)
        if N =="N":
            break
        
        desea = str(input("desea agregar nuevos titulos? (si/no)"))
        if desea == "si":
            agregar(titulos,ejemplares,cantidad_de_titulos)
        else:
             break



