import cv2 as cv

cap=cv.VideoCapture(0)
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
while True:
    ret, frame = cap.read()
    if not(ret):
        break
    frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow('mp4',frame)
    if cv.waitKey(1) & 0XFF == 27:
        break
cv.destroyAllWindows()