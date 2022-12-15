import turtle

t = turtle
t.bgcolor("purple")
t.pencolor("white")
t.pensize(10)
def anjay(xPos, yPos, wow, wiw):
    t.up()
    t.goto(xPos, yPos)
    t.down()
    t.left(70)
    t.forward(wow)
    t.right(135)
    t.forward(wow)
    t.left(70)
    t.forward(wiw)
    t.left(110)
    t.forward(wow)
    t.left(70)
    t.forward(wiw)
    t.color("white")
    t.begin_fill()

anjay(-80, 150, 150, 15)


sc = turtle.Screen().exitonclick()