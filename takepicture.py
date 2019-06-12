
import datetime

def inamecreator():
    currenttime=datetime.datetime.today()
    combinedname="image "+str(currenttime.year)+"-"+str(currenttime.month)+"-"+str(currenttime.day)+" ~"+str(currenttime.hour)+"~"+str(currenttime.minute)+"~"+str(currenttime.second)
    return combinedname



