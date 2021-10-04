import turtle
bob = turtle.Turtle()
bob.speed(0)
def spiral(angle):
    for i in range(40):
        bob.forward(100)
        bob.left(360/angle)
    spiral(4)
   