import numpy as np

N = 100
stock_price = np.random.rand(N) * 100
acc_max = np.maximum.accumulate(stock_price)
max_drawdown = np.min( (stock_price- acc_max) / acc_max) * 100
print(f'Max drawdown: {max_drawdown:.5f}%')
