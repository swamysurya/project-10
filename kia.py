""" accesing vedio footage from mobile camara 
using an ipweb appliction jthat is downloaded from playstore """

import cv2

cap = cv2.VideoCapture('http://192.168.190.31:8080/video')

while True:
    ret, frame = cap.read() #read frame/ image one by ine
    resized = cv2.resize(frame,(600,400))
    cv2.imshow("frame",resized)

    key = cv2.waitKey(1) # wait till key presses
    if key == ord("q"): #after pressing the 'q' keyword in key bioard it break the while
        break
cap.release() # release vedio capture object
cv2.destroyAllWindows() # destroy all frame windows

#please do check the lastr two lines of statements outside the loop

