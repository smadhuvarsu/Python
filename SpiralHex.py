import turtle
import random

colors=['red','orange','yellow','green','blue','purple','hot pink']

turtle.speed(50)
turtle.bgcolor('black')

for i in range(360):
    turtle.pencolor(random.choice(colors))
    turtle.width(i/100+1)
    turtle.fd(i)
    turtle.lt(59)
    
                           
    
    

        
