import turtle
bob = turtle.Turtle()



def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):

    angle = 360/n

    for i in range(n):
        t.fd(length)
        t.lt(angle)

square(bob, 100)

polygon(bob, 9, 70)

turtle.mainloop()
