matriz_temp=[[5,10,20] for i in range(7)]
promedio_sem=0
promedio_dia=0

for i in  range (7):
    promedio_dia += matriz_temp[i][j]
    for j in range (3):
        promedio_sem += matriz_temp[i][j]
        print(promedio_sem/3)
        
print(f"promedio total{promedio_sem/21}, el promedio ")

