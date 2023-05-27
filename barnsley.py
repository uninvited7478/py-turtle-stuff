import turtle
t = turtle.Turtle()
t.pencolor('green')
t.speed(1000)
f = open("dane1.txt", "r")

for line in f:
        x, y = line.split()
        x = 40*float(x)
        y = 40*float(y)
        t.pu()
        t.goto(x, y)
        t.pd()
        t.fd(1)
        
        