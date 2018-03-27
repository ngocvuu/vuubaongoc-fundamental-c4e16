from random import *
from f-math import calc
# import từ eval lỗi No module named "eval"
def generate_quiz():
    err = choice([-1,0,1])
    ops = ["+","-","*","/"]
    op = choice(ops)
    x = randint(0,10)
    # Hint: Return [x, y, op, result]
    result = calc(x,y,op) + err
    return [x, y, op, result]

def check(x, y, op, result, user_choice):
    if user_choice == True:
        if err == 0:
            return True
        else:
            return False
    else:
        if err == 0:
            return False
        else:
            return True
