from eval import calc
from random import randint, choice
x = randint(1,10)
y = randint(1,10)

err = choice([-1, 0, 1])

op = choice(["+", "-", "*", "/"])

# if op == "+":
#     result = x + y
# elif op == "-":
#     result = x - y
# elif op == "*":
#     result = x * y
# elif op == "/":
#     result = x / y

result = calc(x, y, op)
result += err

print("{0} {1} {2} {3} {4}".format(x, op, y, "=", result))

check = input("(Y/N)?")
check.lower()
if err == 0:
    if check == "y":
        print("Yay")
    else:
        print("You're wrong")
else:
    if check == "y":
        print("You're wrong")
    else:
        print("Yay")
