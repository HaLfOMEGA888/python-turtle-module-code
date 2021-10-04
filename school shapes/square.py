import turtle
sq = turtle.Turtle()
sq.pensize(5)
sq.color("black")
sq.fillcolor("Light blue")
sq.begin_fill()
for sqr in [1, 2, 3, 4]:
    sq.forward(100)
    sq.right(90)
sq.end_fill()
