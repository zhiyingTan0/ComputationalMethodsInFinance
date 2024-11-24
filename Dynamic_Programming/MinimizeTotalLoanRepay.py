import numpy as np

# f(X(T)) sum of payments from t all the way to T
# f(x,t) cost-to-go function -- optimized expectation

T = 250 # payment period length
R_min, R_max = 0.01, 0.1 # interest rate bound
B=1.0 #balance
accuracy = 0.01 # accuracy of interpolation
max_refinance=4 # allowed numbers of refinance
R_curr=0.05 # current market / interest rate
delta_R=0.002 # weekly rate change raio
prob_up = prob_down = prob_no_change = 1 / 3

#Rate grid, Balance grid
market_rate_grid = np.arange(R_min, R_max+delta_R,delta_R)
interest_rate_grid = np.arange(R_min, R_max+delta_R, delta_R)
B_grid = np.arange(0, B, 0.01)  # interpolate B
dp_table = np.zeros((len(B_grid), len(market_rate_grid), len(interest_rate_grid), max_refinance+1)) # T=250, all zeros



def next_interest_rate(R, delta_R):
    rates = [R + delta_R, R - delta_R, R]
    # Ensure rates stay within the bounds
    rates = [min(max(r, R_min), R_max) for r in rates]
    probs = [prob_up, prob_down, prob_no_change]
    return rates, probs

def interpolate(B_next, m_rate, f_rate, acc_refinance):
    global dp_table
    lower_B_idx = int(B_next / accuracy) # B_next < 1
    upper_B_idx = min(lower_B_idx + 1, len(B_grid)-1)
    lower_B, upper_B = B_grid[lower_B_idx], B_grid[upper_B_idx]

    m_rate_idx = int((m_rate-R_min) / delta_R)
    f_rate_idx = int((f_rate-R_min) / delta_R)


    lower_cost= dp_table[lower_B_idx, m_rate_idx, f_rate_idx, acc_refinance]
    upper_cost = dp_table[upper_B_idx, m_rate_idx, f_rate_idx, acc_refinance]
    return lower_cost + (B_next - lower_B) / (upper_B - lower_B) * (upper_cost - lower_cost)



def backward_computation():
    #dp_table_next = np.zeros((len(B_grid), len(market_rate_grid), len(interest_rate_grid), max_refinance+1))
    # t from 0 to 249
    global dp_table
    for t in range(T-1, 0, -1):
        dp_table_next = np.zeros((len(B_grid), len(market_rate_grid), len(interest_rate_grid), max_refinance + 1))
        for b_idx, balance in enumerate(B_grid):
            for r_market_idx, r_market in enumerate(market_rate_grid):
                for r_interest_idx, r_interest in enumerate(interest_rate_grid):
                    for acc_refinance in range(max_refinance+1):
                        B_prime = balance * (1.0 + (r_interest / 52))
                        p = B_prime / (T-t)
                        B_next = B_prime-p
                        #next interest rate
                        rates, probs = next_interest_rate(r_market, delta_R)

                        # next possible states
                        """no refinance - market rate may vary"""
                        acc_payment=0
                        for rate, prob in zip(rates, probs):
                            acc_payment += prob*interpolate(B_next, rate, r_interest, acc_refinance)

                        """refinance to market rate"""
                        acc_payment_refinance = acc_payment
                        if acc_refinance < 4:
                            acc_payment_refinance = 0
                            for rate, prob in zip(rates, probs):
                                acc_payment_refinance += prob*interpolate(B_next, rate, r_market, acc_refinance+1)
                       

                        dp_table_next[b_idx, r_market_idx, r_interest_idx, acc_refinance] = p + min(acc_payment_refinance,acc_payment)

        dp_table=dp_table_next
        #print(dp_table[-1, int(R_curr/delta_R), int(R_curr/delta_R), 0])


    return dp_table[-1, int(R_curr/delta_R), int(R_curr/delta_R), 0]

if __name__ == "__main__":
    optimal = backward_computation()
    print(f"Optimal expected cost: {optimal:.5f}")







