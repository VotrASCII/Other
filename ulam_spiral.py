# Ulam Spiral for Prime Numbers

import random
from turtle import *

# prime number generator using Sieve of Eratosthenes
def prime(val):
    p = []
    c = []
    for i in range(2, val+1):
        if i not in c:
            p.append(i)
            for j in range(i*i, val+1, i):
                c.append(j)
    return p


# plot all the prime numbers with black dots
def ulam_spiral(m):
    bgcolor("white")
    hideturtle()
    setposition(0, 0)
    color_selection = ["violet", "indigo", "blue", "green", "orange", "red"]
    val = prime(m)
    count = 0
    j = 1
    penup() # don't want to see the line
    for i in range(1, m):
        for k in range(j):
            if count in val: # prime numbers highlighted by black
                # write(str(count), False, "center")
                pendown()
                dot(7.5, "black")
                penup()
            else: # non-primes by other color
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