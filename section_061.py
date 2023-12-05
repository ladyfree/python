#section_061.py

import turtle

t = turtle.Pen()
t.shape("turtle")

for item in range(30):
    if item%2:
        t.pendown()
    else:
        t.penup()
        
    if item == 10:
        break

    t.forward(10)
    
