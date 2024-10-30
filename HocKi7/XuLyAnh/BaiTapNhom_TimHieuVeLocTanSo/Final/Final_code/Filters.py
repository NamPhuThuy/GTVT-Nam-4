import numpy as np

# HighPass Gaussian
def gen_gaussian_high_pass_filter(D0, U, V):
    """
    Creates a Gaussian high-pass filter kernel in the frequency domain.

    Args:
        D0: The cut-off frequency.
        U: The number of rows in the frequency domain.
        V: The number of columns in the frequency domain.

    Returns:
        The Gaussian high-pass filter kernel.
    """

    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = U // 2
    V0 = V // 2

    for u in range(U):
        for v in range(V):
            #Calculate distance
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2)
            
            #Calculate filter
            H[u, v] = 1 - np.exp(-D[u, v]**2 / (2 * D0**2))
    return H

def gen_gaussian_low_pass_filter(D0, U, V):
    """
    Creates a Gaussian low-pass filter kernel in the frequency domain.

    Args:
        D0: The cut-off frequency.
        U: The number of rows in the frequency domain.
        V: The number of columns in the frequency domain.

    Returns:
        The Gaussian low-pass filter kernel.
    """

    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = U // 2
    V0 = V // 2

    for u in range(U):
        for v in range(V):
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2) #Calculate distance
            H[u, v] = np.exp(-D[u, v]**2 / (2 * D0**2)) #Calculate filter
    return H

def gen_butterworth_high_pass_filter(D0, U, V, n):
    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = U // 2
    V0 = V // 2

    for u in range(U):
        for v in range(V):
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2)
            H[u, v] = 1 / (1 + (D0 / D[u, v])**(2*n))

    return H

def gen_butterworth_low_pass_filter(D0, U, V, n):
    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = U // 2
    V0 = V // 2

    for u in range(U):
        for v in range(V):
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2)
            H[u, v] = 1 / (1 + (D[u, v] / D0)**(2 * n))

    return H

def gen_ideal_high_pass_filter(D0, U, V):
    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = U // 2
    V0 = V // 2

    for u in range(U):
        for v in range(V):
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2)
            if D[u, v] > D0:
                H[u, v] = 1
            else:
                H[u, v] = 0

    return H

def gen_ideal_low_pass_filter(D0, U, V):
    H = np.zeros((U, V))
    D = np.zeros((U, V))
    U0 = U // 2
    V0 = V // 2
    
    for u in range(U):
        for v in range(V):
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2)
            H[u, v] = 1 if D[u, v] <= D0 else 0
    
    return H