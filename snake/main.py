from turtle import Turtle, Screen, color, forward, goto

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CELL_WIDTH = 10
CELL_HEIGHT = 10
BG_COLOUR = 'black'
SN_COLOR = 'white'
FD_COLOR =  'green'

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.fillcolor(SN_COLOR)
        self.shape('square')

def main():
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # screen.tracer(0)

    print(screen.canvheight, " ", screen.canvwidth)
    screen.bgcolor(BG_COLOUR) 

    snake = Snake()
    snake.forward(100)    
    display_grid()
    screen.exitonclick()

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

    for _ in range(int(SCREEN_WIDTH/CELL_WIDTH)):
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

if __name__ == "__main__":
    main()