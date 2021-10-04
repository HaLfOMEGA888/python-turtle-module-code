import turtle
bob = turtle.Turtle()
bob.shape('turtle')
for i in range (4):
    bob.forward(100)
    bob.left(360/4)
bob.penup()
bob.forward(200)
bob.pendown()
bob.circle(30)
