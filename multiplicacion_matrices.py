matriz_A=[[1,2,3],
          [4,5,6],
          [2,5,3]]


matriz_B=[[1,2,5],
          [3,4,3],
          [5,6,7]]


def multiplicacion_matrices(A, B):
    
    if len(A[0]) == len(B):
        
        matriz_C=[]
        for i in range(len(A)):
            matriz_C.append([])
            for j in range(len(B[0])):
                matriz_C[i].append(0)


        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    matriz_C[i][j] += A[i][k]*B[k][j]
        
        return matriz_C
    
    else:
    
        return None

c = multiplicacion_matrices(matriz_A, matriz_B)

if c == None:
    print("No multiplicable")

else:
    for fila in c:
        print("[", end=" ")
        for valor in fila:
            print(valor, end=" ")
        print("]")
