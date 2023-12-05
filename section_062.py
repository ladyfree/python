#section_062.py

import turtle

t = turtle.Pen()
t.shape("turtle")

for item in range(30):
    if item%2:
        t.penup()
        t.forward(10)
        t.pendown()
        continue

    t.forward(10)
    
