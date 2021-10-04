import turtle

oct = turtle.Turtle()
oct.pensize(5)
oct.color("yellow")
oct.fillcolor("orange")
oct.begin_fill()

for p in range(1, 8):
    oct.right(45)
    oct.forward(100)

oct.right(45)
oct.forward(100)

oct.end_fill()
turtle.done()