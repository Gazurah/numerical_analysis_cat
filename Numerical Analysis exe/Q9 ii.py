import numpy as np

def qr_algorithm(A, num_iter=100):
  
    n = A.shape[0]
    Q_total = np.eye(n)
    A_k = A.copy()
    
    for _ in range(num_iter):
        Q, R = np.linalg.qr(A_k)
        A_k = R @ Q
        Q_total = Q_total @ Q
    
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_total
    return eigenvalues, eigenvectors

A = np.array([[4, -2],
              [1,  1]])

eigenvalues, eigenvectors = qr_algorithm(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
