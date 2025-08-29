def area_triangulo (base:float,altura:float):
    return (base*altura)/2
    

b=float(input("ingrese la base del triangulo:"))
a=float(input("ingrese la altura del triangulo: "))
print(area_triangulo(a,b))