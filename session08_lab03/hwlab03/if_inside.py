
# 1. 2 lists as 2 parameters
def is_inside(point =[],rect=[]):


# 2. Check the coordinates of the rectangle and the point
    # if x1 < x < x2 and y1 < y < y2
    if rect[0] < point[0] < rect[0] + rect[2] and rect[1] < point[1] < rect[1] + rect[3]:
        return True
    else:
        return False



# check = is_inside([100,120],[140,60,100,200])
# print(check)
