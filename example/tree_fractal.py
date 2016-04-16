import turtle

# setting up
wn = turtle.Screen()
turtle.setup(500, 400)
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(150)
t.pendown()

def branch(len):
    if len < 10:
        return
    t.forward(len)
    t.left(25)
    branch(len*0.7)
    t.right(50)
    branch(len*0.7)
    t.left(25)
    t.backward(len)

branch(100)

wn.mainloop()
