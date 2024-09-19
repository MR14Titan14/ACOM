import cv2 as cv
import numpy as np

#Задание 1,2
# cap=cv.VideoCapture(0)
# frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#     frame_trash=cv.inRange(frame,(0,100,100),(30,255,255))
#     print(frame[int(frame_width/2)][int(frame_height/2)])
#     cv.imshow('filtered',frame_trash)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
# cv.destroyAllWindows()

#Задание 3
# cap=cv.VideoCapture(0)
# kernel=np.ones((5,5),np.uint8)
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#     frame_trash=cv.inRange(frame,(0,100,100),(30,255,255))
#     opened=cv.morphologyEx(frame_trash,cv.MORPH_OPEN,kernel)
#     closed=cv.morphologyEx(frame_trash,cv.MORPH_CLOSE,kernel)
#     cv.imshow('Open',opened)
#     cv.imshow('Close',closed)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
# cv.destroyAllWindows()

#Задание 4,5
cap=cv.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
while True:
    ret, frame = cap.read()
    if not(ret):
        break
    frameHsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    frameTrash=cv.inRange(frameHsv,(0,155,155),(30,255,255))
    opened=cv.morphologyEx(frameTrash,cv.MORPH_OPEN,kernel)
    openmoments=cv.moments(opened)
    if(openmoments["m00"]!=0):
        print(f"Площадь: {openmoments['m00']}")
        print(f"Моменты 1 порядка: {openmoments['m01']}, {openmoments['m10']}")
        x=int(openmoments['m10']/openmoments['m00'])
        y=int(openmoments['m01']/openmoments['m00'])
        cv.circle(frame,(x,y),10,(0,0,0,),2)
        (contours, _) = cv.findContours(opened.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for countour in contours:
            (x, y, w, h) = cv.boundingRect(countour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 4)
    cv.imshow('Detecting',frame)
    if cv.waitKey(1) & 0XFF == 27:
        break
cv.destroyAllWindows()