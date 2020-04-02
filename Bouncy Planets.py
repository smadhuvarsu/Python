#Boucing Planets

from tkinter import*
import random
import time

shape=input("Hello there! Choose your display. Press 1 for circle, 2 for arc, and 3 for a rectangle:")

#turtle.pensize(3)

colors=["red","orange","yellow","lime green","chartreuse","cyan","magenta","medium blue","deep pink","dark violet"]

WIDTH=1400
HEIGHT=700

tk=Tk()
canvas=Canvas(bg="black",width=WIDTH,height=HEIGHT)
tk.title("Bouncy Planets!")
canvas.pack()

class Planet:
    def __init__(self,color,size):

        if shape=="1":
            self.shape=canvas.create_oval(10,10,size,size,fill=color)

        if shape=="2":
            self.shape=canvas.create_arc(30, 200, 90, 100,fill=color)

        if shape=="3":
            self.shape=canvas.create_rectangle(10, 10, size, size,fill=color)
                              
        self.xspeed=random.randrange(3,20)
        self.yspeed=random.randrange(3,20)

    def move(self):
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)

        if pos[3] >= HEIGHT or pos[1] <=0:
            self.yspeed=-self.yspeed

        if pos[2] >= WIDTH or pos[0] <=0:
            self.xspeed=-self.xspeed

planets=[]
for i in range(100):
    planets.append(Planet(random.choice(colors), random.randrange(50,100)))
    
while True:
    for planet in planets:
        planet.move()
    tk.update()
    time.sleep(0.03)

tk.mainloop()

            




    

