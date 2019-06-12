
import videorecord
import livestream
import timelapse
import welcomepage

def stream():
    livestream.startnstoplive1()

def videowstream():
    livestream.startnstoplive2()

#def timelapsenstream():
#if I have time

def videowstreamwpictures():
    livestream.startnstoplive3()

def scanner():
    
    inpt=input("What would you like to do today?(input corresponding value for what you would like to do)\n1-only livestream\n2-livestream & record video(s)\n3-livestream & record video(s) & take pictures\n")
    if(inpt=="1"):
        print("livestream starting...")
        welcomepage.directions1()
        return stream()    
    elif(inpt=="2"):
        print("livestream & video streamer starting...")
        return videowstream()
        welcomepage.directions2()
    elif(inpt=="3"):
        welcomepage.directions3()
        print("livestream & video streamer & image taking thing starting...")
        return videowstreamwpictures()
    else:
        print("Your input is invalid. Please try again.\n")
        return scanner()
