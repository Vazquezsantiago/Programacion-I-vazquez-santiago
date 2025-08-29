def verificar_acceso(edad):
    if edad >= 18:
        si=True
        print("usted es mayor de edad ")
    else:
        si=False
        print("usted no es mayor de edad ")
        
e=int(input("ingrese su edad: "))

print(verificar_acceso(e))