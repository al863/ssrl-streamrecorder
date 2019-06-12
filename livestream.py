
import numpy as np
import cv2
import videorecord
import takepicture

cam=cv2.VideoCapture(0)
switch=False

def startnstoplive1():
    while(True):
        ret,frame=cam.read()
        cv2.imshow('streamrecorder - livestream only',frame)

        k=cv2.waitKey(1) & 0xFF

        if k==27:
            print("script ended")
            cam.release()
            break

#def get_image():
#    frame=cam.read()
#    return frame

def startnstoplive2():
    videowriter=cv2.VideoWriter("blank.avi",cv2.VideoWriter_fourcc(*'XVID'),int(cam.get(5)),(int(cam.get(3)),int(cam.get(4))))
    global switch
    i=0
    while(True):
        ret, frame=cam.read()
        cv2.imshow('streamrecorder - livestream & video record',frame)

        k=cv2.waitKey(1) & 0xFF
        
        if k==ord('s'):
            switch=True
            print("camera has started recording")
            i+=1
        elif k==ord('q'):
            switch=False
            print("camera has stopped recording")
        
        if(i==1):
            videowriter=videorecord.vwobjectcreator()

        i=videorecord.startnstoprecording(switch,frame,i,videowriter)

        if k==27:
            print("script ended")
            cam.release()
            break

def startnstoplive3():
    videowriter=cv2.VideoWriter("blank.avi",cv2.VideoWriter_fourcc(*'XVID'),int(cam.get(5)),(int(cam.get(3)),int(cam.get(4))))
    global switch
    i=0
    while(True):
        ret,frame=cam.read()
        cv2.imshow('streamrecorder - livestream & video record & pictures',frame)

        k=cv2.waitKey(1) & 0xFF
        
        if k==ord('s'):
            switch=True
            print("camera has started recording")
            i+=1
        elif k==ord('q'):
            switch=False
            print("camera has stopped recording")
        
        if(i==1):
            videowriter=videorecord.vwobjectcreator()

        i=videorecord.startnstoprecording(switch,frame,i,videowriter)

        if k==32:
            currentname=takepicture.inamecreator()
            cv2.imwrite(currentname+".png",frame)
            print(currentname+".png was taken")

        if k==27:
            print("script ended")
            cam.release()
            break

