import numpy as np
from typing_extensions import deprecated

# この関数はオーバーフローの可能性を孕んでいる。
# @deprecated
# def softmax_old(a):
#     exp_a = np.exp(a)
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a

    # return y

def softmax(a):
    max_a = np.max(a)

    exp_a = np.exp(a - max_a) # オーバーフロー対策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
    