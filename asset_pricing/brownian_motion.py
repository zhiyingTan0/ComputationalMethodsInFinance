import numpy as np

""" Brownian motion by Monte Carlo simulation: S_t = S_{t-1} + mu*dt+ sqrt(dt)*sigma*Z where Z ~N(0,1)"""
N =10 # step size
n=100 # sample size
T = 1 # 1 year
mu  = 0.01 #drift
sigma = 0.2 #volatility
dt = T / N #delta T

"""Arithmetic Random Walk / Brownian Motion"""
def brownian_motion(N, n, mu, sigma, dt):
    S0 = np.array([100]*n)
    delta_s = mu*dt + np.random.normal(mu, sigma, (N, n)) * np.sqrt(dt) * sigma
    all_paths=np.cumsum(np.concatenate(S0, delta_s))
    return all_paths


"""Geometric Random Walk / Geometric Brownian Motion"""
def geometric_brownian_motion(N, n, mu, sigma, dt):
    S0 = np.array([100]*n)
    delta_s = np.exp( (mu - sigma**2/2)*dt +np.random.normal(mu, sigma, (N, n)) * np.sqrt(dt) * sigma)
    all_paths = np.cumprod(np.concatenate(S0, delta_s))
    return all_paths









