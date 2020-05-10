import cv2,time
from time import gmtime, strftime
#from datetime import datetime
video=cv2.VideoCapture(0)
face_detect=cv2.CascadeClassifier("E:\python\image processing\haarcascade_front.xml")
a=0
i=1
fourcc=cv2.VideoWriter_fourcc(*'XVID')
print("basic guidelines")
print("C- capture photo")
print("V- Capture Video")
print("O- stopping video capturing")
print("q- stopping program")
print("Let's experience it")
while True:
    a=a+1
    check,frame=video.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
   
    faces=face_detect.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)

    frame2=frame.copy()
    frame2=cv2.resize(frame2,(2976,1984))
    
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("hey me",frame)
    cv2.imshow("hey me",frame)
    key=cv2.waitKey(1)
    
    if key==ord('c'):
        #now=datetime.now()
        #name=str(now.time())+str(".png")
        cv2.imshow("hey me",frame)
        resize=cv2.resize(frame2,(1920,1080))
        name=str(strftime("%Y%m%d%H%M%S", gmtime()))+str(".png")
        cv2.imwrite(name,resize)

    if key==ord('v'):
        #now=datetime.now()
        #name=str(now.time())+str(".mp4")
        name=str(strftime("%Y%m%d%H%M%S", gmtime()))+str(".mp4")
        out=cv2.VideoWriter(name,fourcc,20.2,(640,480))
        while key!=ord('o'):
            
            check,frame=video.read()
            gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            faces=face_detect.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
            frame2=frame.copy()
            #frame2=cv2.resize(frame2,(2976,1984))
    
            for x,y,w,h in faces:
                frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imshow("hey me",frame)
            cv2.imshow("hey me",frame)
            out.write(frame2)
            key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)
video.release()
out.release()
cv2.destroyAllWindows
