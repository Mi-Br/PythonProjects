from turtle import Turtle, Screen, color

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
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
    screen.bgcolor(BG_COLOUR) 

    snake = Snake()
    snake.forward(100)
    screen.exitonclick()

if __name__ == "__main__":
    main()