nombre=input("ingrese su nombre: ")
edad=input("ingrese su edad: ")
numero_de_atracciones=input("ingrese a cuantas atracciones desea subir")

if edad < 6:
    print("solo puede subir al carrusel")
elif edad >= 12:
    print("puede subir a la montaña rusa")
else:
    print("puede subir a todos los juegos")
