import turtle
from random import randint

colors = ("red", "blue","yellow","green","magenta","violet","olive","lime","gold","pink","orange")

lastCol = None
prevCol = None

def RandomCol():
    global lastCol, prevCol
    while True:
        col = colors[randint(0, len(colors)-1)]
        if col != lastCol and col != prevCol:
            prevCol = lastCol
            lastCol = col
            return col
turtle.Turtle()
turtle.pensize(4)

turtle.penup()
turtle.pencolor(RandomCol())
turtle.left(90)   
turtle.forward((turtle.window_height()/2)-20)
turtle.right(90)
turtle.pendown()

sides = 3
count = 0

while True:
    turtle.forward(50)
    turtle.right(360/sides)
    count +=1
    # print("Lados: " + sides)
    if count == sides:
        turtle.pencolor(RandomCol())
        sides += 1
        count = 0



