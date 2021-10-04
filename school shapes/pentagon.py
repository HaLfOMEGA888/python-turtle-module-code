import turtle

pent = turtle.Turtle()
pent.pensize(5)
pent.color("blue")
pent.fillcolor("lightblue")
pent.begin_fill()

for p in range(1,5):
    pent.right(72)
    pent.forward(100)
pent.right(72)
pent.forward(100)

pent.end_fill()
