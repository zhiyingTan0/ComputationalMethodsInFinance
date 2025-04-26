import numpy as np
from scipy.stats import norm

# T = 1 for 1 year maturity
# c: call option price
# p: put option price
# sigma: volatility
# r: risk-free rate
def BS_european_price(S0, K, T, r, sigma):

    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    c = norm.cdf(d1) * S0 - norm.cdf(d2) * K * np.exp(-r * T)
    p = norm.cdf(-d2) * K * np.exp(-r * T) - norm.cdf(-d1) * S0

    return c, p

S0 = 100
K = 105
sigma = 0.2
T = 1.0
r = 0.05

(c,p) = BS_european_price(S0, K, T, r, sigma)
print (f"Black Scholes estimated call option price {c: .5f} and put option price {p: .5f}")