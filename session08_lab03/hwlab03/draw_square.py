from turtle import *
def draw_square(length,color):
    fillcolor(color)
    for i in range(4):
        forward(length)
        right(90)
        return length,color
    mainloop()
# draw_square(100, "green")
