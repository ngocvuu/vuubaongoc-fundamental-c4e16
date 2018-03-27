# from random import choice
# x = 3
# op = choice(["+", "-", "*", "/"])
# y = 7
#
# result = -999
#
# if op == "+":
#     result = x + y
# elif op == "-":
#     result = x - y
# elif op == "*":
#     result = x * y
# else:
#     result = x / y
#
# print(result)

from random import choice

def calc(x, y, op):

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else:
        result = x / y
    return result

# res = calc(3, 7, "+")
# print(res)
#
# r = calc(1, 2, "-")
# print(r)
# argument, parameter
# calc()
# op = choice(["+", "-", "*", "/"])
# calc(3, 7, "-")
