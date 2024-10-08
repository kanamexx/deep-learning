def AND(x1: int, x2: int) -> int:
    w1,w2,theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    

def NAND(x1: int, x2: int) -> int:
    w1,w2,theta = -0.5, -0.5, -0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1: int, x2: int) -> int:
    w1,w2,theta = 1, 1, 0.9
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1