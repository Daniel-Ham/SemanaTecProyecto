import numpy as np 

print ('Escriba el valor deseado')
V = int(input())

import cv2
from numpy import zeros
import matplotlib.pyplot as plt
import numpy as np
im=cv2.imread('imagen.jpg')
im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
#im = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)

def gris(im):
	gray= np.zeros((im.shape[0],im.shape[1]))
	for i in range(im.shape[0]):
		for j in range(im.shape[1]):
			temp = 0
			for k in range(im.shape[2]):
				temp += im[i, j, k]
			gray[i,j]= temp/3
	return gray

def validacionV(a):
	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			if int(a[i][j]) > V:
				a[i][j] = 1
			else:
				a[i][j] = 0
	return a

B= np.array([[1,1,1],[1,0,1],[1,1,1]])
a = gris(im)

#print(a)
#print(a.shape)

imagenBN = validacionV(a)
#imagenBN = validacionV(im)

#cv2.imwrite("imagenBN.jpg",imagenBN)
cv2.imwrite("imagenGR.jpg", a)
