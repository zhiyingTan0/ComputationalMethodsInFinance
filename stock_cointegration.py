import numpy as np
from statsmodels.tsa.stattools import coint

n = 100
x = np.cumsum(np.random.normal(0, 1, n))  # Random walk
y = 0.5 * x + np.random.normal(0, 1, n)    # Cointegrated with x

score, p_value, _ = coint(x, y)

print(f"Cointegration Score (ADF Test Statistic): {score:.4f}")
print(f"P-value: {p_value:.4f}")

# --- Step 3: Interpret ---
if p_value < 0.05:
    print("The two series are likely cointegrated. Suitable for pairs trading.")
else:
    print("No strong evidence of cointegration. Not ideal for pairs trading.")