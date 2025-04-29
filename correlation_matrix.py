import numpy as np

"""Cholesky decomposition: L*L.T is PSD where L is lower triangular matrix"""

def generate_random_correlation_matrix(dim):
    """
    Generate a random valid correlation matrix of size (dim x dim) by Cholesky decomposition
    """

    # Step 1: Generate a random symmetric positive definite matrix
    # a lower triangular matrix
    L = np.tril(np.random.rand(dim, dim))
    # Cholesky decomposition to form covariance matrix
    positive_definite_matrix = np.dot(L,L.T)

    # Step 2: Normalize to create a correlation matrix
    # d is covariance matrix
    d = np.sqrt(np.diag(positive_definite_matrix))  # cov(xi, xi) (sqrt of variances)
    variance_matrix = np.array([[var] for var in d]) # form n by 1 matrix
    # sqrt(Var_xi) * sqrt(Var_xj)
    correlation_matrix = positive_definite_matrix / np.dot(variance_matrix, variance_matrix.T)  # Normalize to get correlations
    np.fill_diagonal(correlation_matrix, 1)  # correlation of same variable should be 1

    return correlation_matrix

def is_valid_correlation_matrix(matrix):
    """
    Verify the validity of a correlation matrix.

    Parameters:
    - matrix (numpy.ndarray): A correlation matrix to verify.

    Returns:
    - bool: True if the matrix is valid, False otherwise.
    """
    # Check symmetry , atol is the allowing difference
    if not np.allclose(matrix, matrix.T, atol=1e-8):
        return False

    # Check all diagonal elements are 1
    if not np.allclose(np.diag(matrix), 1, atol=1e-8):
        return False

    # Check positive semi-definiteness
    eigenvalues = np.linalg.eigvals(matrix)
    if np.any(eigenvalues < -1e-8):  # Small negative values can occur due to numerical precision
        return False

    return True



dim = 6
random_corr_matrix = generate_random_correlation_matrix(dim)
is_valid = is_valid_correlation_matrix(random_corr_matrix)