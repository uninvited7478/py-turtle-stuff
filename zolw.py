import turtle
from random import randrange

turtle.bgcolor("black")


t = turtle.Turtle()
t1 = turtle.Turtle()

t.penup()
t.color('green')
t.goto(250, -200)
t.pendown()
t.pencolor('green')
t.goto(250, 200)
t.penup()
t1.penup()
t1.pencolor("blue")
t1.goto(-300, -100)
t.goto(-300, 100)
t.color("red")
t.pencolor("red")
t.pendown()
t1.pendown()
while(1):
    tur = randrange(15)
    tur1 = randrange(15)
    t.forward(tur)
    t1.forward(tur1)
    if(t.xcor() > 250):
        t.write("WYGRALEM!")
        break
    if(t1.xcor() > 250):
        t1.write("WYGRALEM!")
        break


turtle.exitonclick()
    







