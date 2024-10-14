import numpy as np

print('=== A ===')
A = np.array([1, 2, 3, 4])
print(A)

print(np.ndim(A))
print(A.shape)
print(A.shape[0])

print('=== B ===')
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B))
print(B.shape)
print(B.shape[0])

print('=== C ===')
C = np.array([[1,2], [3,4]])
D = np.array([[5,6], [7,8]])
print(np.dot(C, D))