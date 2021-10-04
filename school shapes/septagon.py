import turtle

septa = turtle.Turtle()
septa.pensize(5)
septa.color("violet")
septa.fillcolor("purple")
septa.begin_fill()

for p in range(1, 7):
    septa.right(51.42)
    septa.forward(100)
septa.right(51.42)
septa.forward(100)

septa.end_fill()