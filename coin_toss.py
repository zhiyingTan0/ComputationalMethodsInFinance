import numpy as np

N = 10000
events=np.random.binomial(N, 0.5)
print(f'Flipping a coin, probability of H is {events/N: .5f}')