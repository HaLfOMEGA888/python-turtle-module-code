import turtle
hex = turtle.Turtle()
hex.pensize(5)
hex.color('blue')
hex.fillcolor('lightblue')
hex.begin_fill()

for p in range (1,6):
    hex.right(60)
    hex.forward(100)

hex.right(60)
hex.forward(100)

hex.end_fill()
