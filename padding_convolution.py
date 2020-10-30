import cv2
import numpy as np

def padding_conv(A,B):
    C = np.zeros((len(A), len(A[0])))
    suma = 0
    zero = np.zeros((len(A) + 2, len(A[0]) + 2))
    
   

    for i in range(1,len(zero) -1):
        for j in range(1,len(zero[0]) -1):
            zero[i][j] = A[i-1][j-1]
    print(zero)



    for i in range(len(C)):
        for j in range(len(C[0])):
            suma = 0
            for iaux in range(len(B)):
                for jaux in range(len(B[0])):
                    suma += zero[i+iaux][j+jaux]*B[iaux][jaux]
                    if suma > 255:
                        suma = 255
            C[i][j] = suma
 


    return C
matrix = [[1,0,0.5,0.5],[0,0.5,1,0],[0,1,0.5,1],[1,0.5,0.5,1]]
A = np.array(matrix)
filtro = [[1,0],[0,0.5]]
B = np.array(filtro)
print(padding_conv(A,B))
imagen = cv2.imread('imagen.jpg')
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
kernel = [[3,4,3],[1,0,1],[2,3,1]]
K = np.array(kernel)
print(padding_conv(imagen,K))
cv2.imwrite('imagenpruebapadding.jpg',padding_conv(imagen,K))

