from tkinter import *
from random import *


class Ball:
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
        self.__xVel = randint(-5,5)
        self.__yVel = randint(-5,5)

    def move(self):
        self.__x += self.__xVel
        self.__y += self.__yVel
        
        self.__canvas.coords(self.__ball, self.__x, self.__y,
                             self.__x+self.__size, self.__y+self.__size)
