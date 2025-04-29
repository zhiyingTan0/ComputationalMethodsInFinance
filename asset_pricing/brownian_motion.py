import numpy as np

""" Brownian motion by Monte Carlo simulation: S_t = S_{t-1} + mu*dt+ sqrt(dt)*sigma*Z where Z ~N(0,1)"""
N =10 # step size
n=100 # sample size
T = 1 # 1 year
mu  = 0.01 #drift
sigma = 0.2 #volatility
r = 0.025
Sb = 110
K = 105
S0 = 100
# dt = T / N #delta T

"""Arithmetic Random Walk / Brownian Motion"""
def brownian_motion(N, n, mu, sigma, dt):
    S0 = np.array([100]*n)
    delta_s = mu*dt + np.random.normal(mu, sigma, (N, n)) * np.sqrt(dt) * sigma
    all_paths=np.cumsum(np.concatenate(S0, delta_s))
    return all_paths


"""Geometric Random Walk / Geometric Brownian Motion"""
def geometric_brownian_motion(s0, N, n, mu, sigma, dt):
    S0 = np.array([s0]*n)
    delta_s = np.exp( (mu - sigma**2/2)*dt +np.random.normal(mu, sigma, (N, n)) * np.sqrt(dt) * sigma)
    all_paths = np.cumprod(np.concatenate((S0, delta_s), axis =0 ))
    return all_paths

def MC_barrier_knockin_price(S0, Sb, K, T, r, mu, sigma, n, N):
    s = geometric_brownian_motion(S0, N, n, mu, sigma, T/N)
    knock_in = np.any(s  > Sb, axis = 0)

    call_payoff = np.maximum(s[len(s)-1]-K,0)
    put_payoff = np.maximum(K-s[len(s)-1],0)

    c = np.mean(np.where(knock_in, call_payoff, 0)) * np.exp(-r*T)
    p = np.mean(np.where(knock_in, put_payoff, 0)) * np.exp(-r*T)

    return c, p
c , p = MC_barrier_knockin_price(S0, Sb, K, T, r, mu, sigma, n, N)
print(f'Call Price = {c:.5f} and Put Price = {p:.5f}')








