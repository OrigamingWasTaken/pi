import os
import pathlib
import turtle
import random

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

file = pathlib.Path("./messages.txt")
lines = file.open().read().split('\n')

message = lines[random.randrange(0,len(lines))]

r = lambda: random.randint(0,255)
color = '#%02X%02X%02X' % (r(),r(),r())

screen = turtle.Screen()
screen.title("Message of the day")
screen.setup(width = 1.0, height = 1.0, startx=None, starty=None)
screen.bgcolor("cyan")

font = ("Helvetica", 30)
label = turtle.write("Hi!", font=font)

turtle.done()