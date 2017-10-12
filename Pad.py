from tkinter import *


class Pad:
    def __init__(self, canvas, x, y, x2, y2, color):
        self.__canvas = canvas
        self.__xEdge = int(canvas.cget('width'))
        self.__yEdge = int(canvas.cget('height'))
        self.__x = x
        self.__y = y
        self.__x2 = x2
        self.__y2 = y2
        self.__color = color
        self.__pad = canvas.create_rectangle(x, y, x2, y2, fill=color)
        self.__canvas.itemconfig(self.__pad, fill=color, outline=color)
        self.__canvas.bind('<Button-1>', self.moveLeft)
        self.__canvas.bind('<Button-2>', self.moveRight)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def moveLeft(self, event):
        self.__x -= 40
        self.__canvas.coords(self.__pad, self.__x, self.__y,
                             self.__x + 100, self.__y + 20)


    def moveRight(self, event):
        self.__x += 40
        self.__canvas.coords(self.__pad, self.__x, self.__y,
                             self.__x + 100, self.__y + 20)
