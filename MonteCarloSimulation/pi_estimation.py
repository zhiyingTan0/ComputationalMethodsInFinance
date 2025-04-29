import numpy as np

N = 10000
# A = np.random.rand(N*2).reshape((N,2)) # N points (x,y)
A = np.random.rand(N,2)
pts_in_circle = np.sum(A[:, 0]**2 + A[:, 1]**2 <= 1)
print("Estimated pi is:", 4*pts_in_circle/N)

