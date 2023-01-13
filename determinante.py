import numpy as np 

matriz= np.array([[5, 2, 5],
                  [3, 4, 2],
                  [7, 6, 2]]) 

det = np.linalg.det(matriz) 
  
print("La determinante es:\n") 
print(int(det)) 