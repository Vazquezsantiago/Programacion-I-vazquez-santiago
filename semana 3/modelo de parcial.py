from funciones_vectores import *

numero_participantes=0
participantes=[""]*10
puntuacion=[0]*10
comentario=[""]*10
while True:
    print("--- Menú Encuesta de Satisfacción ---")
    print("1. Ingresar participantes")
    print("2. Mostrar participantes y promedio")
    print("3. Ordenar participantes por puntuación")
    print("4. Salir")
    seleccion = input("Seleccione una opción (1-4): ")
    if seleccion == "1":
        ingresar(numero_participantes, participantes, puntuacion, comentario)
        pass
    elif seleccion == "2":
        mostrar(participantes, puntuacion, comentario)
        pass
    elif seleccion == "3":
        pass
    elif seleccion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")