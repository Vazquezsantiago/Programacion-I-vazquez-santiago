from funciones_vectores import ingresar

numero_participantes=0
participantes=0

while True:
    print("--- Menú Encuesta de Satisfacción ---")
    print("1. Ingresar participantes")
    print("2. Mostrar participantes y promedio")
    print("3. Ordenar participantes por puntuación")
    print("4. Salir")
    seleccion = input("Seleccione una opción (1-4): ")
    if seleccion == "1":
        ingresar(numero_participantes,participantes)
        pass
    elif seleccion == "2":
        pass
    elif seleccion == "3":
        pass
    elif seleccion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")