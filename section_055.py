#section_055.py

import turtle

t = turtle.Pen()
t.shape("turtle")

draw = True
if draw :
    t.forward(100)

if not draw :
    t.forward(-100)

moyang = 3
if moyang == 4 :
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
else :
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
