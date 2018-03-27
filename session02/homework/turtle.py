#cau hoi 1 trong turtle exercise c lam ko dc nha Quy :<
from turtle import *
shape("arrow")
for i in range(3,7):
    for j in range(i):
        forward(100)
        left(360/i)

        if i % 2 == 0:
            color("blue")
        else:
            color("red")

mainloop()
