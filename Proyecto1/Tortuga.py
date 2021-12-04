import turtle

turtle.Turtle()

sides = 3
movement = 50

turtle.pencolor("red")
turtle.fillcolor("green")
turtle.pensize(4)

while True:
    turtle.forward(movement)    
    turtle.right(360/sides)
    movement +=1
    