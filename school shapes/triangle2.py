import turtle
t2 = turtle.Turtle()
t2.pensize(5)
t2.color("blue")
t2.fillcolor("Light blue")
t2.begin_fill()
for tri in [1, 2]:
    t2.forward(100)
    t2.right(90)
t2.right(45)
t2.forward(143)
t2.end_fill()
