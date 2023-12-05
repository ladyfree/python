#section_053.py

import turtle

t = turtle.Pen()
t.shape("turtle")

legs = input('거북이의 다리 갯수는? ')
legs = int(legs)
skin = input('거북이의 색은? ')

if legs == 4 and skin == 'green' :
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
if legs == 4 or skin == 'black' :
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)

    
