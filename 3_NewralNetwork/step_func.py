import numpy as np

def step_function(x):
    # if x > 0:
    #     return 1
    # else:
    #     return 0
    # 
    # 以下は冗長な例。正しく動くけど。
    # astype(int)の暗黙の型変換: astype(int)は、Trueを1、Falseを0に変換しますが、NumPy配列に対しては、dtypeをintに変換するという意味になります。そのため、意図した動作にならない可能性があります。
    # y = x > 0
    # return y.astype(int)

    # こちらの方がパフォーマンスがよいらしい。
    return np.where(x > 0, 1, 0)