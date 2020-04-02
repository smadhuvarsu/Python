import cv2
import numpy as np
import pygame

pygame.init() 

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
eyeDetect=cv2.CascadeClassifier('haarcascade_eye.xml');
cam=cv2.VideoCapture(0);

while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    eyes=eyeDetect.detectMultiScale(gray,1.3,5);
    face_found=False
    eye_found=False

    for(x,y,w,h) in faces:
        face_found=True
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

        '''if face_found==True:
        #face_count=(len(faces))
        #print(face_count, "face(s) found. Hello!")
         face_found = False
    elif face_found==False:
        #print("Nobody seen.")'''

    for(x,y,w,h) in eyes:
        eye_found=True
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow("Facial Recognition",img);
        
    if(cv2.waitKey(1)==ord('q')):
        pygame.time.delay(10)
        face_count=(len(faces))
        print(face_count, "face(s) found. Hello!")

        pygame.time.delay(10)
        eye_count=(len(eyes))
        print(eye_count, "happy eye(s) found.")
        break;

cam.release()
cv2.destroyAllWindows()
