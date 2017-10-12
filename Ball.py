from tkinter import *
from random import *
from Block import *


class Ball:

    numOfBalls = 0

    def __init__(self, canvas, x, y, size, color):
        self.__canvas = canvas
        self.__xEdge = int(canvas.cget('width'))
        self.__yEdge = int(canvas.cget('height'))
        self.__x = x
        self.__y = y
        self.__size = size
        self.__color = color
        self.__ball = canvas.create_oval(x, y, x+size, y+size)
        self.__canvas.itemconfig(self.__ball, fill=color, outline=color)
        self.__xVel = 4
        self.__yVel = 4
        Ball.numOfBalls += 1

    def move(self, pad, someBlocks):
        self.__x += self.__xVel
        self.__y += self.__yVel

        self.__canvas.coords(self.__ball, self.__x, self.__y,
                             self.__x + self.__size, self.__y + self.__size)

        if self.__x <= 0 or self.__x + self.__size >= self.__xEdge:
            self.__xVel *= -1

        if self.__y <= 0:
            self.__yVel *= -1

        if (pad.x < self.__x <= pad.x + 100) and (self.__y + self.__size >= pad.y):
            self.__yVel *= -1


        for block in someBlocks:
            if (block.x <= self.__x <= block.x + 50) and self.__y <= block.y + 20:
                block.remove()
                self.__yVel *= -1
                block.x = 0
                block.y = 0

        if Block.numOfBlocks == 0:
            import sys
            sys.exit(0)

        if Ball.numOfBalls == 0:
            import sys
            sys.exit(0)
