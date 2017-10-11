from tkinter import *
from time import *
from Ball import *
from random import *


WIN_SIZE = [850,500]
NUM_BALLS = 10

root = Tk()
canvas = Canvas(width = WIN_SIZE[0], height = WIN_SIZE[1], bg = 'black')
canvas.grid(row=0,column=0)
color = ['red', 'blue', 'green', 'yellow', 'white']

someBalls = []

for i in range(NUM_BALLS):
    ball = Ball(canvas, randint(100, WIN_SIZE[0]-100), randint(100, WIN_SIZE[1]-100),
                randint(10, 100), color[randint(0,4)])
    someBalls.append(ball)


def motion():
    for aBall in someBalls:
        aBall.move()
    root.after(25, motion)


motion()

root.mainloop()
