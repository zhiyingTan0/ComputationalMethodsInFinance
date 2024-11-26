# Problem Description

1. Write a program that uses the **Box-Muller algorithm** to generate independent standard normal random variables. Test whether the program produces the density by generating a large number of Gaussian samples and placing them into bins. The bin size is \( \Delta x \).  

   - The \( k^{\text{th}} \) bin is defined as:
     \[
     B_k = \left(x_k - \frac{\Delta x}{2}, x_k + \frac{\Delta x}{2}\right)
     \]
     where \( x_k = k \Delta x \).  
   - If we generate \( N \) samples, the \( k^{\text{th}} \) "bin count" \( N_k \) is the number of \( X_j \) that fall into \( B_k \) for \( j = 1, \ldots, N \).  

   - The expected bin counts are given by:
     \[
     \mathbb{E}[N_k] = N \int_{B_k} f(x) dx,
     \]
     where \( f(x) \) is the probability density function (PDF) of a standard normal distribution.

2. If the bins are small enough, the integrals in the above equation can be approximated using **Taylor series expansions** of \( f(x) \) about \( x_k \). Using one or two terms should suffice.  

3. Create a plot showing the actual bin counts and the expected bin counts. If \( \Delta x \) is fixed and \( N \) is large enough, these plots should agree within small statistical errors.

4. To test whether the Box-Muller algorithm produces **independent Gaussian variables**, create pairs \( (X_j, Y_j) \), generate bins in 2D, and compare empirical bin counts to expected bin counts. Use the **joint density function** for independent standard normal distributions.  

   - The bin \( B_{kl} \) in 2D is a square centered at \( (x_k, y_l) \) with side length \( \Delta x \).
