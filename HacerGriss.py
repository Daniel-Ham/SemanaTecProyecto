import cv2
from numpy import zeros
import matplotlib.pyplot as plt
import numpy as np
im=cv2.imread('imagen.jpg')
def gris(im):
    gray= zeros((im.shape[0],im.shape[1]))
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            temp=0
            temp =int(im[i,j,0])+int(im[i,j,1])+int(im[i,j,2])
            gray[i,j]= temp/3
            print(gray)
            return gray


def ConvolusionSinP(gray,B):
    C=zeros((gray.shape[0]-2,gray.shape[1]-2))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            temp=0
            for ii in range(B.shape[0]):
                for jj in range(B.shape[1]):
                    temp+=gray[ii+i][jj+j]*B[ii][jj]
                C[i][j]=temp
    return C            
B= np.array([[1,1,1],[1,0,1],[1,1,1]])
imagenG1=ConvolusionSinP(gris(im),B)
cv2.imwrite("imagenG1.jpg",imagenG1)





