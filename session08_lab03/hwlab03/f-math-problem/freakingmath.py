from random import *
from fmath import calc
# import từ eval bị lỗi No module named
def generate_quiz():
    err = choice([-1,0,1])
    ops = ["+","-","*","/"]
    op = choice(ops)
    x = randint(0,10)
    y = randint(0,10)
    # Hint: Return [x, y, op, result]
    result = calc(x,y,op) + err
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if result == calc(x,y,op):
            return True
        else:
            return False
    else:
        if result == calc(x,y,op):
            return False
        else:
            return True
