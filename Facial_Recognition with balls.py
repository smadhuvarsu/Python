import cv2
import numpy as np
import pygame
import random
import time
import tkinter
from tkinter import*
import PIL.Image, PIL.ImageTk
pygame.init()
pygame.mixer.init()

def balls():
    colors=["red","orange","yellow","lime green","chartreuse","aqua","magenta","medium blue","deep pink","dark violet"]
    WIDTH=1400
    HEIGHT=700
    tk=Tk()
    canvas=Canvas(bg="black",width=WIDTH,height=HEIGHT)
    tk.title("Bouncy Planets!")
    canvas.pack()

    class Planet:
        def __init__(self,color,size):
            self.shape=canvas.create_oval(10,10,size,size,fill=color)
            self.xspeed=random.randrange(3,30)
            self.yspeed=random.randrange(3,30)
        def move(self):
            canvas.move(self.shape,self.xspeed,self.yspeed)
            pos=canvas.coords(self.shape)


            if pos[3] >= HEIGHT or pos[1] <=0:
                self.yspeed=-self.yspeed
            if pos[2] >= WIDTH or pos[0] <=0:
                self.xspeed=-self.xspeed

    planets=[]
    for i in range(150):
        planets.append(Planet(random.choice(colors), random.randrange(30,100)))
        
    while True:
        for planet in planets:
            planet.move()
        tk.update()
        time.sleep(0.03)

    tk.mainloop()

class App:
    def __init__(self, window, window_title, image_path="NoEntryFinal4.jpg"):
        self.window = window
        self.window.title(window_title)
        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape
        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.mainloop()


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
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        face_found=True
  
    for(x,y,w,h) in eyes:
        eye_found=True
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

    if (eye_found==True) or (face_found==True):
        if(cv2.waitKey(1)==ord('s')):
                pygame.time.delay(10)
                balls()

    if (eye_found==False) or (face_found==False):
        if (cv2.waitKey(1)==ord('s')):
                pygame.time.delay(10)
                # Create a window and pass it to the Application object
                App(tkinter.Tk(), "Tkinter and OpenCV")


 
    cv2.imshow("Click 's' to find an animation when your face is detected ; click 'q' to quit the program.",img);
    
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
