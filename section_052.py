#section_052.py

import turtle

t = turtle.Pen()
t.shape("turtle")

side1 = 100
side2 = 50
if side1 > 0 :
    t.forward(side1)

if side1 >= side2 :
    t.up()
    t.forward(side2)
    t.down()
    t.forward(side1)

if 60 < side2 <= side1 :
    t.reset()
