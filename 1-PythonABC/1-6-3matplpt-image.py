
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../data/lena.png')
plt.imshow(img)

plt.show()