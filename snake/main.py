from turtle import Turtle, Screen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CELL_WIDTH = 10
CELL_HEIGHT = 10
BG_COLOUR = 'black'


s = Screen()
s.setup(SCREEN_WIDTH, SCREEN_HEIGHT, 'BG_COLOUR')


s.bgcolor('black') 
s.screensize(100, 100, 'yellow')

t = Turtle()
s.exitonclick()


def main():
    print("Hello, World!")

    t = Turtle()
    t.forward(10)

if __name__ == "__main__":
    main()