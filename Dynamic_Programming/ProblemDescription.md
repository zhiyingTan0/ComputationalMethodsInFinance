### **Objective:**

To explore dynamic programming.

---

This is a qualitative model. It is unrealistic in several ways in order to be as simple as possible. We suppose that a floating interest rate fluctuates between **1%** and **10%** (annualized). Now it is **5%**. Each week it may move up or down by **0.2%**, except that it is blocked from moving outside its range. It moves in either direction with probability **1/3** and remains unchanged with this probability. All movements are independent. This interest rate is **R(t)**.

A loan of **$1** is to be repaid in **250 weeks**. Each week, we add some interest and make a payment. If our interest rate at week **t** is **r(t)**, and the outstanding balance is **B(t)**, then, at week **t**, we first add interest, replacing:

**B(t)** by:

**B'(t) = (1 + r(t)/52) * B(t)**.

Next, we make a prorated payment:

**P(t) = B'(t) / (250 - t)**.

This leaves:

**B(t+1) = B'(t) - P(t)**.

Our interest rate is determined as follows. At week **0**, **r(t) = R(t) = 5%**. However, **r(t)** remains fixed until we "refinance." Whenever we refinance, **r(t)** is replaced by **R(t)**.

We are allowed to refinance up to **four times** during this **250-week period**. We want to do so to minimize our total expected payments:

**E[P(0) + P(1) + ... + P(249)]**.

---

### Task

1. Set this up as a dynamic programming problem.
2. Identify the state space. Ans: X[B, r_market, r_interest, refinance_count]
3. Write a computer program to solve it by dynamic programming.
4. Use interpolation to estimate unknown values of the cost-to-go function from previously computed values.
    Ans: f(x,t) the optimized expectation of accumulated payment from t to T