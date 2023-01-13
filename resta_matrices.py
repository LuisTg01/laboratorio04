matriz_A = []
matriz_B = []
resta_matriz=[]

filas=int(input("Introduce el número de filas: "))
columnas=int(input("Introduce el número de columnas: "))


for i in range(filas):
    matriz_A.append([0]*columnas)
    

for i in range(filas):
    matriz_B.append([0]*columnas)


for i in range(filas):
    resta_matriz.append([0]*columnas)

#Cambiamos los valores de las matrices

for i in range(filas):
    for j in range(columnas):
        matriz_A[i][j]=int(input("Ingrese los componentes de A:(%d, %d): "%(i+1,j+1)))

for i in range(filas):
    print(matriz_A[i])



for i in range(filas):
    for j in range(columnas):
        matriz_B[i][j]=int(input("Ingrese los componentes de B:(%d, %d): "%(i+1,j+1)))

for i in range(filas):
    print(matriz_B[i])



for i in range(filas):
    for j in range(columnas):
        resta_matriz[i][j]=matriz_A[i][j]+matriz_B[i][j]

print("\n")
print("Resultado:")
print("\n")
for i in range(filas):
    R=[]
    for j in range(columnas):
        R.append(resta_matriz[i][j])
    
    print(R)
