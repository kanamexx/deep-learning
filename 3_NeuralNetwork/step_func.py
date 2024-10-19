import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    # if x > 0:
    #     return 1
    # else:
    #     return 0
    # 
    # 以下は冗長な例。正しく動くけど。
    # y = x > 0
    # return y.astype(int)

    # こちらの方がパフォーマンスがよいらしい。
    return np.where(x > 0, 1, 0)

# 3-2-3 グラフ描画
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y軸の範囲を指定
plt.show()


print("tst")
x = np.array([
    [0.1, 0.8, 0.1],
    [0.3, 0.1, 0.6],
    [0.2, 0.5, 0.3],
    [0.8, 0.1, 0.1]])

max = np.argmax(x, axis=0)
print(max)