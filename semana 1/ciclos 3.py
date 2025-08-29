edad=int(input("ingrese su edad: "))
for juego in range (3):
    juego = str(input("¿a que juego desea subir?: "))
    if juego == ("montaña rusa") and edad >= 12:
        print("puede subir a la montaña rusa")
