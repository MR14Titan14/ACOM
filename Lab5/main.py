import cv2 as cv

def process(path,thrashLow,thrashAr,ksize,sigma):
    cap = cv.VideoCapture(path, cv.CAP_ANY)
    ret, frame = cap.read()
    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    video_writer = cv.VideoWriter("output.mp4", fourcc, 25, (w, h))
    ret,frame=cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    oldframe = cv.GaussianBlur(gray, (ksize, ksize), sigma)
    while True:
        ret, frame = cap.read()
        if not (ret):
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gaus = cv.GaussianBlur(gray, (ksize, ksize), sigma)
        frame_diff = cv.absdiff(oldframe, gaus)
        thrash = cv.threshold(frame_diff, thrashLow, 255,cv.THRESH_BINARY)[1]
        contours,_=cv.findContours(thrash,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

        try:
            cnt=contours[0]
            area = cv.contourArea(cnt)
            if area > thrashAr:
                video_writer.write(frame)
        except:
            print("Нет контура")
        oldframe = gaus
    cap.release()
    cv.destroyAllWindows()
process("test1.mp4",200,30,3,100)