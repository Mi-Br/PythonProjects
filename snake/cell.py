from turtle import Turtle
from const import *

class Cell(Turtle):
    def __init__(self,x=CELL_WIDTH/2,y=CELL_HEIGHT/2):
        super().__init__()
        self.penup()
        self.fillcolor(SN_COLOR)
        self.shape('square')
        self.pensize(CELL_WIDTH)
        self.shapesize(.5,.5,0)
        self.goto(x,y)

