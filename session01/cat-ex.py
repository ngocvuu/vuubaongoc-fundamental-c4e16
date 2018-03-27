from turtle import *

shape("turtle")
speed(-1)
# color("green")
fillcolor("black")

number = int(input("How many sides do you want for your pentagon?"))

begin_fill()
for i in range(number):
    ####
    forward(100)
    left(360/number)
    ####
end_fill()
mainloop()
