import cv2 as cv

#Задание 2
# img1 = cv.imread("test.png",cv.IMREAD_COLOR)
# img2 = cv.imread("test.jpeg",cv.IMREAD_GRAYSCALE)
# img3 = cv.imread("test.raw",cv.IMREAD_ANYDEPTH)


# cv.namedWindow("PNG",cv.WINDOW_AUTOSIZE)
# cv.imshow("PNG", img1)
# cv.waitKey(0) # Wait for a keystroke in the window
# cv.destroyAllWindows()
# cv.namedWindow("JPEG",cv.WINDOW_FULLSCREEN)
# cv.imshow("JPEG", img2)
# cv.waitKey(0) # Wait for a keystroke in the window
# cv.destroyAllWindows()
# cv.namedWindow("RAW",cv.WINDOW_GUI_EXPANDED)
# cv.imshow("RAW", img3)
# cv.waitKey(0) # Wait for a keystroke in the window
# cv.destroyAllWindows()

#Задание 3
# cap=cv.VideoCapture(r'vidt.mp4',cv.CAP_ANY)
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     cv.imshow('mp4',gray)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
#
# cap1=cv.VideoCapture(r'vidt.mp4',cv.CAP_ANY)
# while True:
#     ret1, frame1 = cap1.read()
#     if not(ret1):
#         break
#     cv.imshow('mov',frame1)
#     if cv.waitKey(1) & 0XFF == 27:
#         break

#Задание 4
# cap=cv.VideoCapture(r'vidt.mp4',cv.CAP_ANY)
# ret,frame=cap.read()
# w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# video_writer = cv.VideoWriter("output.mp4", fourcc, 25, (w, h))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv.imshow('mp4',frame)
#     video_writer.write(frame)
#     if cv.waitKey(1) & 0XFF == 27:
#         break
# cap.release()
# cv.destroyAllWindows()

#Задание 5
# img1 = cv.imread("vershina1.jpg",cv.IMREAD_COLOR)
# hsv = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
# cv.imshow('orig',img1)
# cv.imshow('hsv',hsv)
# cv.waitKey(0) # Wait for a keystroke in the window
# cv.destroyAllWindows()

#Задание 6
# cap=cv.VideoCapture(0)
# frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     startp1=(int(frame_width/2)-15,int(frame_height/2)-60)
#     endp1=(int(frame_width/2)+15,int(frame_height/2)+60)
#     startp2=(int(frame_width/2)-60,int(frame_height/2)-15)
#     endp2=(int(frame_width/2)+60,int(frame_height/2)+15)
#     rec1=cv.rectangle(frame,startp1,endp1,(0,0,255),2)
#     res=cv.rectangle(rec1,startp2,endp2,(0,0,255),2)
#     cv.imshow('mp4',res)
#     if cv.waitKey(1) & 0XFF == ord('q'):
#         break
# cv.destroyAllWindows()

#Задание 7
# cap=cv.VideoCapture(0)
# ret,frame=cap.read()
# w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# video_writer = cv.VideoWriter("camoutput.mp4", fourcc, 25, (w, h))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv.imshow('mp4',frame)
#     video_writer.write(frame)
#     if cv.waitKey(1) & 0XFF == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

#Задание 8
# cap=cv.VideoCapture(0)
# frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     startp1=(int(frame_width/2)-15,int(frame_height/2)-60)
#     endp1=(int(frame_width/2)+15,int(frame_height/2)+60)
#     startp2=(int(frame_width/2)-60,int(frame_height/2)-15)
#     endp2=(int(frame_width/2)+60,int(frame_height/2)+15)
#     blue,green,red=frame[int(frame_width/2)][int(frame_height/2)]
#     color=(blue,green,red)
#     max_val = max(color)
#     max_index = color.index(max_val)
#     color=tuple(255 if i == max_index else 0 for i, x in enumerate(color))
#     print(color)
#     rec1=cv.rectangle(frame,startp1,endp1,color,-1)
#     res=cv.rectangle(rec1,startp2,endp2,color,-1)
#     cv.imshow('mp4',res)
#     if cv.waitKey(1) & 0XFF == ord('q'):
#         break
# cv.destroyAllWindows()

#Задание 9
# cap=cv.VideoCapture("rtsp://192.168.0.70:8080/h264_pcm.sdp")
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv.imshow('mp4',frame)
#     if cv.waitKey(1) & 0XFF == 27:
#         break