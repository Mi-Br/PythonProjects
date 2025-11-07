from turtle import Turtle, Screen
from const import *
from grid import display_grid
from cell import Cell 

class Snake():
    def __init__(self):
        self.body = [Cell(x*CELL_WIDTH) for x in range(3)]
        # self.goto(CELL_HEIGHT/2, CELL_WIDTH/2)
    
def main():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    print(screen.canvheight, " ", screen.canvwidth)
    screen.bgcolor(BG_COLOUR) 

    snake = Snake()
    # display_grid()
    screen.exitonclick()

if __name__ == "__main__":
    main()