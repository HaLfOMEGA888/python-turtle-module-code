#PROGRAM TO DRAW 5 PENTAGON CIRCLE
import turtle
bob = turtle.Turtle()
bob.shape("square")
bob.speed(0)
bob.color("blue")
for i in range (100):
    bob.circle(i)
bob.left(360/5)