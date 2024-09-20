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

    blured=img.copy()
    Start = kernelSize // 2

    for i in range(Start, blured.shape[0] - Start):
        for j in range(Start, blured.shape[1] - Start):
            val=0
            for k in range(-Start, Start + 1):
                for l in range(-Start, Start + 1):
                    val += img[i + k, j + l] * kernel[k + Start, l + Start]
            blured[i, j] = val
    return blured

img=cv.imread("jak.jpeg",cv.IMREAD_GRAYSCALE)
blured1=gausianBlur(img,5,100)
blured2=gausianBlur(img,7,100)
blured3=gausianBlur(img,5,10)
blured4=gausianBlur(img,7,10)

cv.imshow("blured 5 100",blured1)
cv.imshow("blured 7 100",blured2)
cv.imshow("blured 5 10",blured3)
cv.imshow("blured 7 10",blured4)

cv.waitKey(0) # Wait for a keystroke in the window
cv.destroyAllWindows()