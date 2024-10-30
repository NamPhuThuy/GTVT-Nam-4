import numpy as np
import matplotlib.pyplot as plt
import cv2
import cmath

# Định nghĩa hàm biến đổi DFT
def dft_1d(img):
    U = len(img) #U = 8
    
    #Outarry [0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j]
    outarry = np.zeros(U, dtype=complex)
    
    for m in range(U):
        sum = 0.0
        for n in range(U):
            e = np.exp(-1j * 2 * np.pi * m * n / U)
            sum += img[n] * e
            #print(f"  [{m,n}]: img[{n}]={img[n]}, exp={e}, accumulated sum={sum}")
        outarry[m] = sum
        #print(f"DFT[{m}] = {outarry[m]}")
    return outarry


def idft_1d(img):
    U = len(img)
    outarry = np.zeros(U, dtype = complex)
    for n in range(U):
        sum = 0.0
        for m in range(U):
            e = np.exp(1j * 2 * np.pi * m * n / U)
            sum += img[m] * e
            # print(f"accumulated sum = {sum}")
        pixel = sum / U
        outarry[n] = pixel
        # print(f"DFT[{m}] = {outarry[m]}")
    return outarry


def dft_2d(img):
    """
    Custom implementation of 2D Discrete Fourier Transform.
  
    Args:
        img: A 2D numpy array representing the image.
  
    Returns:
        The 2D Fourier Transform of the image.
    """

    M, N = img.shape
    F = np.zeros((M, N), dtype=complex)

    for u in range(M):
        for v in range(N):
            sum = 0
            for x in range(M):
                for y in range(N):
                    # Calculate the exponential term
                    exp_term = np.exp(-2j * np.pi * (u * x / M + v * y / N))
                    # Add the contribution of each pixel
                    sum += img[x, y] * exp_term
            # Store the result at frequency (u, v)
            F[u, v] = sum
    return F



def idft_2d(F):
    M, N = F.shape
    f = np.zeros((M, N), dtype=complex)
    for x in range(M):
        for y in range(N):
            sum = 0
            for u in range(M):
                for v in range(N):
                    sum += F[u, v] * np.exp(2j * np.pi * (u*x/M + v*y/N))
            f[x, y] = sum / (M * N)
    return f.real

def fft_shift(X):
    """
    Custom implementation of frequency shift.
  
    Args:
        X: A 2D numpy array representing the data to be shifted.
  
    Returns:
        The shifted array with the zero-frequency component in the center.
    """

    M, N = X.shape
    return np.roll(np.roll(X, -M // 2, axis=0), -N // 2, axis=1)

def my_abs(X):
    """
    Custom implementation of absolute value for complex numbers.
    """
    return np.sqrt(X.real**2 + X.imag**2)