from funciones_vectores import *
cantidad_de_titulos=0
cantidad_de_titulos = int(input("ingrese cuantos titulos son: "))
titulos= [0]*cantidad_de_titulos
ejemplares= [0]*cantidad_de_titulos

N=""
while N != "N":
        for i in range(cantidad_de_titulos):
            print("----menu de opciones----")
            t = str(input("ingresar titulo: "))
            e = int(input("ingrese cuantos ejemplares "))
            titulos[i]= t
            ejemplares[i]= e
            N=input(str("ingrese N para salir"))
            if N =="N":
                break
mostrar(titulos,ejemplares)
desea = str(input("desea agregar nuevos titulos? (si/no)"))
if desea == "si":
     agregar(titulos,ejemplares)

modificar(titulos, ejemplares)


        
