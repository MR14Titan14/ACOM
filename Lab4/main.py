import cv2 as cv
import numpy as np


def kanny(path,kernelSize,sigma):
    img = cv.imread(path, cv.IMREAD_GRAYSCALE)
    cv.imshow("grayscale", img)
    gaus = cv.GaussianBlur(img, (kernelSize, kernelSize), sigma)
    cv.imshow("gaussian", gaus)
    cv.waitKey(0)
    cv.destroyAllWindows()
    length = np.zeros(gaus.shape)
    angle = np.zeros(gaus.shape)
    for x in range(1, (len(gaus) - 1)):
        for y in range(1, len(gaus[0]) - 1):
            Gx = gaus[x + 1][y + 1] - gaus[x - 1][y - 1] + gaus[x + 1][y - 1] - gaus[x - 1][y + 1] + 2 * (
                    gaus[x + 1][y] - gaus[x - 1][y])
            Gy = gaus[x + 1][y + 1] - gaus[x - 1][y - 1] + gaus[x - 1][y + 1] - gaus[x + 1][y - 1] + 2 * (
                    gaus[x][y + 1] - gaus[x][y - 1])
            length[x][y] = np.sqrt(Gx * Gx + Gy * Gy)
            tg = np.arctan(Gy / Gx)
            # print(Gx,Gy,tg)
            if 0 < Gx and Gy < 0 and tg < -2.414 or Gx < 0 and Gy < 0 and tg > 2.414:
                angle[x][y] = 0
            elif Gx > 0 and Gy < 0 and tg < -0.414:
                angle[x][y] = 1
            elif (Gx > 0 and Gy < 0 and tg > -0.414) or (Gx > 0 and Gy > 0 and tg < 0.414):
                angle[x][y] = 2
            elif Gx > 0 and Gy > 0 and tg < 2.414:
                angle[x][y] = 3
            elif (Gx > 0 and Gy > 0 and tg > 2.414) or (Gx < 0 and Gy > 0 and tg < -2.414):
                angle[x][y] = 4
            elif Gx < 0 and Gy > 0 and tg < -0.414:
                angle[x][y] = 5
            elif (Gx < 0 and Gy > 0 and tg > -0.414) or (Gx < 0 and Gy < 0 and tg < 0.414):
                angle[x][y] = 6
            elif Gx < 0 and Gy < 0 and tg < 2.414:
                angle[x][y] = 7

    cv.imshow("lengths", length)
    cv.imshow("angles", angle)
    cv.waitKey(0)
    cv.destroyAllWindows()
    maxLength = np.max(length)
    borders=np.zeros(gaus.shape)
    for x in range(1, (len(gaus) - 1)):
        for y in range(1, len(gaus[0]) - 1):
            ix = 0
            iy = 0
            if (angle[x][y] == 0):
                iy = -1
            if (angle[x][y] == 1):
                iy = -1
                ix = 1
            if (angle[x][y] == 2):
                ix = 1
            if (angle[x][y] == 3):
                iy = 1
                ix = 1
            if (angle[x][y] == 4):
                iy = 1
            if (angle[x][y] == 5):
                iy = 1
                ix = -1
            if (angle[x][y] == 6):
                ix = -1
            if (angle[x][y] == 7):
                iy = -1
                ix = -1
            border=length[x][y]>length[x+ix][y+iy] and length[x][y]>length[x-ix][y-iy]
            borders[x][y]=255 if border else 0
    cv.imshow("borders",borders)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    lowLevel=maxLength//1.0250
    highLevel=maxLength//1.0200

    for x in range(1, (len(gaus) - 1)):
        for y in range(1, len(gaus[0]) - 1):
            if(borders[x][y]==255):
                if(length[x][y]<lowLevel):
                    borders[x][y]=0
    for x in range(1, (len(gaus) - 1)):
        for y in range(1, len(gaus[0]) - 1):
            if(borders[x][y]==255):
                if(length[x][y]<=highLevel):
                    if(borders[x-1][y-1]==255 or borders[x-1][y]==255 or borders[x-1][y+1]==255 or borders[x][y+1]==255 or borders[x+1][y+1]==255 or borders[x+1][y]==255 or borders[x+1][y-1]==255 or borders[x][y-1]==255):
                        borders[x][y] = 255
                    else:
                        borders[x][y] = 0
    cv.imshow("borders filtered", borders)
    cv.waitKey(0)
    cv.destroyAllWindows()

kanny("oi.png",5,100)
