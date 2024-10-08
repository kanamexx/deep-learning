
import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(0, 6, 0.1) # 0から6まで0.1刻みで生成
y = np.sin(x)

# グラフの描画
plt.plot(x, y)
plt.show()

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")

plt.xlabel("x")
plt.xlabel("y")
plt.title('sin & cos')

plt.legend()
plt.show()
