def power_iteration(A, num_iter=100):
    
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_iter):
        b_k1 = np.dot(A, b_k)
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
    
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    eigenvector = b_k
    return eigenvalue, eigenvector

# Example matrix
A = np.array([[4, -2],
              [1,  1]])

# QR algorithm
eigenvalues_qr, eigenvectors_qr = qr_algorithm(A)
print("QR Algorithm Eigenvalues:", eigenvalues_qr)
print("QR Algorithm Eigenvectors:\n", eigenvectors_qr)

# Power iteration
eigenvalue_power, eigenvector_power = power_iteration(A)
print("\nPower Iteration Dominant Eigenvalue:", eigenvalue_power)
print("Power Iteration Dominant Eigenvector:\n", eigenvector_power)
