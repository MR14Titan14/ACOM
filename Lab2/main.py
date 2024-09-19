import cv2 as cv

#Задание 1,2
cap=cv.VideoCapture(0)
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
while True:
    ret, frame = cap.read()
    if not(ret):
        break
    frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    frame_trash=cv.inRange(frame,(0,100,100),(30,255,255))
    print(frame[int(frame_width/2)][int(frame_height/2)])
    cv.imshow('mp4',frame_trash)
    if cv.waitKey(1) & 0XFF == 27:
        break
cv.destroyAllWindows()