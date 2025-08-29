
def convertir_minutos(min:int):
   horas = min//60
   mini = min-horas*60
   return(min,"minutos es",horas,"horas y", mini,"minutos")

minutos=int(input("ingrese los minutos: "))

print(convertir_minutos(minutos))
           