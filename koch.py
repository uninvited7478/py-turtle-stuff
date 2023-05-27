import turtle

t = turtle.Turtle()
t.speed(1000)

def koch(bok, n):
    if n == 1:
        t.fd(bok)
    else:
        koch(bok/3, n-1)
        t.lt(60)
        koch(bok/3, n-1)
        t.rt(120)
        koch(bok/3, n-1)
        t.lt(60)
        koch(bok/3, n-1)

def platek(bok, n):
    t.pu()
    t.bk(180)
    t.pd()
    for i in range(3):
        koch(bok, n)
        t.rt(120)


platek (200,4)