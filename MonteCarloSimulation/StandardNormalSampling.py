import math
import numpy as np
import matplotlib.pyplot as plt
"""
    Divide the sampling N(0,1) generated with Box Muller algorithm into K bin: B_k
    Compare with actual expected E[B_k]
"""

delta_x = 0.05 # bin size
N = 10000 # number of samples X1, X2, ..... XN
K = 25 # number of bins

def generate_gaussian_samples(N):
    # Uniform distribution
    U1 = np.random.uniform(0, 1, N)
    U2 = np.random.uniform(0, 1, N)

    # normal distribution
    Z1 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
    Z2 = np.sqrt(-2 * np.log(U1)) * np.sin(2 * np.pi * U2)

    return Z1, Z2

def bin_counts(sample, delta_x, K):
    bins = np.arange(-0.5*delta_x, K*delta_x, delta_x)
    counts, edges = np.histogram(sample, bins=bins)
    #bin_centers = np.arange(1,N)
    return counts


def expected_bin_counts(K, delta_x):
    """Taylor Series Expansion of 3 terms: F(x) = F(0) + x / sqrt(2pi) - x^3 / 6*sqrt(2pi)"""
    bins = np.arange(-0.5 * delta_x, K * delta_x, delta_x)
    expected_counts = np.zeros(K)
    for i in range(K):
        # calculate DF of Bk bin by taylor expansion
        x1 = bins[i+1]
        x0 = bins[i]
        df_Bk = ((0.5 + x1/math.sqrt(2*math.pi)-math.pow(x1,3)/(6*math.sqrt(2*math.pi))) -
                 (0.5 + x0/math.sqrt(2*math.pi)-math.pow(x0,3)/(6*math.sqrt(2*math.pi))))
        print(df_Bk)
        expected_counts[i] = N * df_Bk
    return expected_counts



Z1_sample, Z2_sample = generate_gaussian_samples(N)
bin_counts = bin_counts(Z1_sample, delta_x, K)
expected_bin_counts = expected_bin_counts(K, delta_x)

plt.figure(figsize=(10, 6))
print(bin_counts.size)
plt.bar(np.arange(1,K+1), bin_counts, width=delta_x, alpha=0.5, label="Actual Counts")
plt.plot(np.arange(1,K+1), expected_bin_counts, 'r-', lw=2, label="Expected Counts")
plt.title("N(0,1) Sampling Bin: Actual vs Expected")
plt.xlabel("Kth Bin")
plt.ylabel("Count")
plt.legend()
plt.grid()
plt.show()