import turtle
bob = turtle.Turtle()
bob.shape('square')
bob.speed(0)
for i in range (100):
    bob.forward(i)
    bob.left(360/5)