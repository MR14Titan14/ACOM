import cv2 as cv
import numpy as np

def kanny(path):
    img=cv.imread(path,cv.IMREAD_GRAYSCALE)
    cv.imshow("grayscale",img)
    gaus=cv.GaussianBlur(img,(5,5),100)
    cv.imshow("gaussian",gaus)
    cv.waitKey(0)
    cv.destroyAllWindows()

kanny("oi.png")