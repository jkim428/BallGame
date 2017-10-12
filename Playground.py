from tkinter import *
from time import *
from Ball import *
from Pad import *
from Block import *
from random import *


WIN_SIZE = [700, 700]
NUM_BALLS = 30
NUM_BLOCKS = 5

root = Tk()
canvas = Canvas(width=WIN_SIZE[0], height=WIN_SIZE[1], bg='black')
canvas.grid(row=0, column=0)
color = ['red', 'blue', 'green', 'yellow', 'white']

someBalls = []
someBlocks = set()

for i in range(NUM_BALLS):
    #ball = Ball(canvas, randint(100, WIN_SIZE[0] - 100), randint(100, WIN_SIZE[1] - 100),
                #randint(10, 100), color[randint(0, 4)])
    ball = Ball(canvas, randint(100, WIN_SIZE[0] - 100), randint(100, WIN_SIZE[1] - 100),
                10, 'yellow')

    someBalls.append(ball)


pad = Pad(canvas, WIN_SIZE[0] / 2 - 50, WIN_SIZE[1] - 50, WIN_SIZE[0] / 2 + 50, WIN_SIZE[1] - 30, 'white')


blockX = 50
blockY = 50

for i in range(NUM_BLOCKS):
    block = Block(canvas, blockX, blockY, blockX + 50, blockY + 20, 'red')
    blockX += 60
    someBlocks.add(block)


def motion():
    for aBall in someBalls:
        aBall.move(pad, someBlocks)
    root.after(25, motion)



motion()

root.mainloop()


