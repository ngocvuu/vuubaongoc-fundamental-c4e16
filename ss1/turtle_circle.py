from turtle import *
speed(-1)
shape("triangle")
color("green")

circles = int(input("How many circles?"))
for i in range(circles):
    left(360/circles)
    circle(100)

mainloop()
