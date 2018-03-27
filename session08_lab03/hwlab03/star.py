from turtle import *

def draw_star(x,y,length):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

    return x, y, length
    mainloop()
# draw_star(34, -110, 200)
