def calcular_edad(anio_nacimiento):
    edad=2025-anio_nacimiento
    return("tu edad es:", edad)

anio=int(input("ingrese su edad: "))
print(calcular_edad(anio))
