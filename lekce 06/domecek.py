from turtle import forward, left, right, exitonclick, shape, penup, pendown
shape('turtle')
import math

def domecek(delka):
    for i in range(2):
        forward(delka)
        left(135)   
        forward(math.sqrt(2*delka**2))
        left(135)
        forward(delka)
        left(90)
        forward(delka)
        left(90) 
    right(45)
    forward(math.sqrt(2*delka**2)/2)
    left(90)
    forward(math.sqrt(2*delka**2)/2)
    left(135)
    forward(delka)
    exitonclick()

domecek(200)

