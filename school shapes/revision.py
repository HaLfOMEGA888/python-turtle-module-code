#revision for assessments
import turtle
d1 = turtle.Turtle()
d1.shape("turtle")
d1.pensize(5)
d1.fillcolor("cyan")
d1.begin_fill()
for i in range (4):
   d1.forward(100)
   d1.left(360/4)
d1.end_fill()
d1.fillcolor("red")
d1.begin_fill()
d1.circle(40)
d1.end_fill()
d1.forward(150)
d1.fillcolor("blue")
d1.begin_fill()
for b in range(3):
    d1.forward(110)
    d1.right(120)
d1.end_fill()