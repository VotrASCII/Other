from turtle import *
import random

color_selection = ['violet', 'indigo', 'blue', 'green', 'orange', 'yellow', 'red']

def tree(branchLen, t):
    color(color_selection[random.randint(0, 6)])
    if branchLen > 1:
        forward(branchLen)
        right(20)  # change to 45 and you got a beautiful necklace
        tree(branchLen-10, t)
        left(40)  # change to 45 and you got a beautiful necklace
        tree(branchLen-10, t)
        right(20)  # change to 45 and you got a beautiful necklace
        backward(branchLen)

def main():
    reset()
    t = Turtle()
    hideturtle()
    bgcolor('black')
    title('FRACTAL Tree')
    setposition(0, -100)
    left(90)
    penup()
    backward(30)
    pendown()
    tree(90, t)
    exitonclick()

if __name__ == '__main__':
    main()