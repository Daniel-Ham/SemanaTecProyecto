import numpy as np
import cv2


#funcion que calcula la matriz resultante C después de aplicar la operacion de convolucion de A*B
def convolution(A,B):
    C = np.zeros((len(A) - 2, len(A[0]) - 2))
    suma = 0 
    for i in range(len(C)):
        for j in range(len(C[0])):
            suma = 0 
            for iaux in range(len(B)):
                for jaux in range(len(B[0])):
                    suma += A[i + iaux][j + jaux]*B[iaux][jaux]
            C[i][j] = suma
    
    return C #convolution matrix

Matrix1 = [[6,0,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro = [[1,0,2],[5,0,9],[6,2,1]]
A = np.array(Matrix1)
B = np.array(Filtro)
#C = np.zeros((2,2))
convolution(A,B)
Matrix2 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
Filtro2 = [[1,1,1],[0,0,0],[2,10,3]]
D = np.array(Matrix2)
E = np.array(Filtro2)
print(convolution(D,E))
#print(Matrix1)
print(A)
print(A[1][0]) 
print(convolution(A,B))
imagen  = cv2.imread('imagen.jpg')
#imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
filtro = [[1,1,1],[1,0,1],[1,1,1]]
F = np.array(filtro)
im = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
cv2.imwrite('imagenpruebaconv.jpg',convolution(im,F))
Matrix = [[10,4,50,30,20],[80,0,0,0,6],[0,0,1,16,17],[0,1,0,7,23],[1,0,6,0,4]]
m1 = np.array(Matrix)
filtro1 = [[1,0,1],[0,0,0],[1,0,3]]
f1 = np.array(filtro1)

print(convolution(m1,f1))
