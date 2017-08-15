# Ulam Spiral for Fibonacci Numbers

import random
from turtle import *

# fibonacci
def fibonacci(val):
    f = [0, 1]
    value, i = 0, 2
    while i <= val:
        value = f[i-1] + f[i-2]
        f.append(value)
        i += 1
    return f

# plot all the prime numbers with black dots
def ulam_spiral(m):
    title("ULAM SPIRAL Fibonacci")
    bgcolor("white")
    hideturtle()
    setposition(0, 0)
    color_selection = ["violet", "indigo", "blue", "green", "orange", "red"]
    val = fibonacci(m)
    count = 0
    j = 1
    penup()  # don't want to see the line
    for i in range(1, m):
        for k in range(j):
            # fibonacci numbers highlighted by black
            if count in val:
                # write(str(count), False, "center")
                pendown()
                dot(7.5, "black")
                penup()
            else: # non-fibonacci by other color
                pendown()
                dot(3.5, color_selection[random.randint(0, 5)])
                penup()
            count += 1
            forward(10)
        left(90)
        j += 1


# user input and function invoking
def main():
    input_val = int(input("Enter a number \n"))
    ulam_spiral(input_val)


if __name__ == '__main__':
    main()