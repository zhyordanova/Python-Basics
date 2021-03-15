import turtle

my_turtle = turtle.Turtle()

my_turtle.shape("turtle")

my_turtle.color("red", "yellow")

turtle.begin_fill()

while True:
    my_turtle.forward(200)
    my_turtle.left(170)

    if abs(my_turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()
