import cv
import numpy as np
cap=cv.VideoCapture(0)
lower_range=np.array([])
upper_range=np.array([])
while True:
    ret,frame=cap.read()
    frame=cv.resize(frame,(640,480))
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV) 
    mask=cv.inRange(hsv,lower_range,upper_range)
    _,mask1=cv.threshold(mask,254,255,cv.THRESH_BINARY)
    cnts,_=cv.findContours(mask1,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv.contourArea(c)>x:
            x,y,w,h=cv.boundingRect(c)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(frame,("DETECT"),(10,60),cv.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
            
    cv.imshow("FRAME",frame)
    if cv.waitKey(1)&0xFF==27:
        break
cap.release()
cv.destroyAllWindows()
