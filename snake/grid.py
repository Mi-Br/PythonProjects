from turtle import Turtle
from const import *

def display_grid():
    startx =  -SCREEN_WIDTH/2
    starty =  SCREEN_HEIGHT/2
    # endy = starty - SCREEN_HEIGHT + CELL_HEIGHT
    
    gturtl = Turtle()
    gturtl.color('white')
    gturtl.right(90) 
    gturtl.penup()
    gturtl.goto(startx,starty)
    gturtl.speed('fastest')

    for _ in range(int(SCREEN_WIDTH/CELL_WIDTH)+1):
        gturtl.goto(startx,starty)
        gturtl.pendown()
        gturtl.forward(SCREEN_HEIGHT)
        gturtl.penup()
        startx = startx + CELL_WIDTH
    
    startx =  -SCREEN_WIDTH/2
    starty =  SCREEN_HEIGHT/2

    gturtl.penup()
    gturtl.goto(startx,starty)
    gturtl.left(90)
    for _ in range(int(SCREEN_WIDTH/CELL_WIDTH)):
        gturtl.pendown()
        gturtl.forward(SCREEN_WIDTH)
        gturtl.penup()
        starty = starty - CELL_HEIGHT
        gturtl.goto(startx,starty)
