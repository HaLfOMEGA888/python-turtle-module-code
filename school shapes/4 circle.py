#PROGRAM TO DRAW 4 CIRCLES WITH USER DEFINED FUNCTION IN 4 QUDRANTS
import turtle
bob = turtle.Turtle()
def c4(color):
    """This function will draw a circle"""
    bob.fillcolor(color)
    bob.begin_fill()
    bob.circle(40)
    bob.end_fill()
bob.pu()
bob.goto(150,150)
bob.pd()
c4("red")
bob.pu()
bob.goto(-150,150)
bob.pd()
c4("green")
bob.pu()
bob.goto(-150,-150)
bob.pd()
c4("yellow")
bob.pu()
bob.goto(150,-150)
bob.pd()
c4("blue")
