
import numpy as np
import cv2
import datetime
import livestream


def vnamecreator():
    currenttime=datetime.datetime.today()
    combinedname=str(currenttime.year)+"-"+str(currenttime.month)+"-"+str(currenttime.day)+" ~"+str(currenttime.hour)+"~"+str(currenttime.minute)+"~"+str(currenttime.second)
    return combinedname

def vwobjectcreator():
    global cam
    frame_width=livestream.cam.get(3)
    frame_heigth=livestream.cam.get(4)
    fps=livestream.cam.get(5)
    vwobject=cv2.VideoWriter(vnamecreator()+".avi",cv2.VideoWriter_fourcc(*'XVID'),int(fps),(int(frame_width),int(frame_heigth)))
    return vwobject    

def startnstoprecording(bool,mat,int,VideoWriter):
    i=int;
    
    if (bool):
        i+=1
    if(i>1):    
        if (bool):
            VideoWriter.write(mat)
        if(bool==False):
            VideoWriter.release()
            i=0
            print("videorecording stopped.")
    return i

