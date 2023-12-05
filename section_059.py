#section_059.py

import turtle

star = turtle.Pen()
star.shape("turtle")

for k in range(40) :
    star.forward(k * 10)
    star.right(144)
    
