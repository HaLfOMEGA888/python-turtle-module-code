import turtle
bob = turtle.Turtle()
def c(color,size,color2,size2,sides,angle):
    bob.fillcolor(color)
    bob.begin_fill()
    for i in range(sides):
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()
    bob.backward(70)
    bob.fillcolor(color2)
    bob.begin_fill()
    bob.circle(size2)
    bob.end_fill()
bob.pu()
bob.goto(150,150)
c("blue",50,"green",10,5,360/5)
bob.goto(-150,150)
c("green",40,"blue",30,8,360/8)
bob.goto(150,-150)
c("pink",60,"purple",60,4,360/4)
bob.goto(-150,-150)
c("purple",30,"pink",40,3,360/3)