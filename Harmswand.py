# OpenCV import
import cv2
import numpy as np

#Frames setzen
FPS = 250
#Tasten zum Beenden setzen
BREAK_KEYS = (27, ord('Q'), ord('q'))

def main():
    #Webcam wählen 
    cap = cv2.VideoCapture(1)
    img_counter = 0
    
    #Dauerschleife der Webcam
    while True:
        k = cv2.waitKey(1)
        success, frame = cap.read()
        
        if success:
            #Farbe
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            #Farbbereich der angezeigt werden soll
            lower_green = np.array([0,80,0])
            upper_green = np.array([150,250,150])
            
            #Bereich wird in 0 und 1 unterteilt (Schwarz und Weiß)
            mask = cv2.inRange(hsv, lower_green, upper_green)
            #Nur 1 werden normal angezeigt
            res = cv2.bitwise_and(frame, frame, mask = mask)
            
            #3 Fenster der Webcam werden geöffnet
            cv2.imshow('Orignal', frame)
            cv2.imshow('mask' , mask)
            cv2.imshow('res' , res)
        
        #Bei Leertaste wird das momentane Bild gespeichert
        if k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name)) 
            img_counter += 1
            
        #Abbruch des Programms    
        if (cv2.waitKey(1000 // FPS) & 0xff) in BREAK_KEYS:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

