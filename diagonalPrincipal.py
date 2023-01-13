M=[[4,8,6],
   [5,2,3],
   [7,0,1]]

suma = 0
#diagonal principal
print("diagonal principal")
for d in range(len(M)):
    diag = M[d][d]
    print(diag)
    suma +=diag

#diagonal secundaria
print("Segunda diagonal")
for d in range(len(M)):
    diag = M[d][-d-1]
    print(diag)
    suma +=diag
print(f"suma:{suma}")