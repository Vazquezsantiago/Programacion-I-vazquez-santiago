def mostrar():
    return print("montaña rusa, casa del terror, carrusel")


def puede_subir(edad:int,atraccion:str):
    if edad >= 12 and atraccion == "montaña rusa":
        print("puede subir a", atraccion)
    elif edad < 12 and atraccion == "montaña rusa":
        print("No puede subir a", atraccion)

    elif atraccion == "carrusel":
        print(" puede subir a", atraccion)

    elif edad > 6 and atraccion == "casa del terror":
        print("puede subir a", atraccion)
    elif edad < 6 and atraccion == "casa del terror":
        print("No puede subir a", atraccion)

def calcular_precio(atraccion:str):
    if atraccion == "montaña rusa":
        precio=1500
    elif atraccion == "casa del terror":
        precio=1200
    elif atraccion == "carrusel":
        precio = 800

    print("$",precio)


def registrar_visita(nombre,atraccion1,atraccion2,atraccion3):
    if atraccion1 or atraccion2 or atraccion3 == "montaña rusa":
        motañarusa=+1
        print("te subiste a la montaña rusa")
    if atraccion1 or atraccion2 or atraccion3 == "carrusel":
        carrusel=+1
        print("te subiste a carrusel")
    if atraccion1 or atraccion2 or atraccion3 == "casa del terror":
        casa=+1
        print("te subiste a casa del terror")

        

    
print(registrar_visita)



def mostrar_resumen(nombre:str,atraccion1:str,atraccion2:str,atraccion3:str):

    print("¡chau", nombre,"!")
    print("visitaste ", atraccion1, atraccion2, atraccion3)
    print("gracias por su visita vuelva pronta :)")

