#section_060.py

import turtle

t = turtle.Pen()
t.shape("turtle")
t.up()

colors = ['red', 'green', 'blue', 'yellow', 'purple']
for c in colors :
    t.color(c)
    for i in range(12) :
        t.forward(100)
        t.dot()
        t.backward(100)
        t.right(30)
    t.right(6)
