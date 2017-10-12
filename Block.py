from tkinter import *


class Block:

    numOfBlocks = 0

    def __init__(self, canvas, x, y, x2, y2, color):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__x2 = x2
        self.__y2 = y2
        self.__color = color
        self.__block = canvas.create_rectangle(x, y, x2, y2, fill=color)
        self.__canvas.itemconfig(self.__block, fill=color, outline=color)
        Block.numOfBlocks +=1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def remove(self):
        self.__canvas.delete(self.__block)
        Block.numOfBlocks -= 1
