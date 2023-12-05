#section_056.py

import turtle

t = turtle.Pen()
t.shape("turtle")

color = int(input('색을 선택하세요(1:파랑, 2:빨강, 3:노랑): '))

if color == 1 :
    t.pencolor("blue")
elif color == 2 :
    t.pencolor("red")
elif color == 3 :
    t.pencolor("yellow")
else :
    t.pencolor("black")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
