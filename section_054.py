#section_054.py

import turtle

t = turtle.Pen()
t.shape("turtle")

reptilia = ['turtle', 'crocodile', 'iguana', 'chameleon']
amphibian = ['frog', 'toad', 'axolotl']

if 'turtle' in reptilia:
    t.color('gray')
    t.forward(100)

if 'turtle' not in amphibian:
    t.color('lightgray')
    t.forward(100)
