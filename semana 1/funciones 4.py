def buscar_mayor(num1:int,num2:int,num3:int):
 if num1 >= num2 or num1>= num3:
     if num2 >= num3:
        return(num1,num2,num3)
     elif num2<=num3:
        return(num1,num3,num2)

 elif num3 >= num1 or num3 >= num2:
    if num1>=num2:
       return(num3,num1,num2)
    else:
       return(num3,num2,num1)

 elif num2 >= num3 or num2 >= num1:
    if num3 >= num1:
       return(num2,num3,num1)
    else:
       return(num2,num1,num3)


a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
c=int(input("ingrese un numero: "))

print(buscar_mayor (a, b, c))
