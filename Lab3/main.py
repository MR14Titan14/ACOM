import cv2 as cv
import numpy as np

#Задание 1
def gauss(x, y, omega, a, b):
    first = 1/(2*np.pi * (omega ** 2))
    second = np.exp(-((x-a) ** 2 + (y-b) ** 2) / (2*(omega**2)))

    return first * second

def gausianBlur(img,kernelSize,devation):
    kernel=np.ones((kernelSize,kernelSize))
    a=b=(kernelSize+1)//2
    for i in range(kernelSize):
        for j in range(kernelSize):
            kernel[i,j]=gauss(i,j,devation,a,b)
    print(kernel)
    sum=kernel.sum()
    kernel/=sum
    print(kernel)

    
gausianBlur(5,10)
