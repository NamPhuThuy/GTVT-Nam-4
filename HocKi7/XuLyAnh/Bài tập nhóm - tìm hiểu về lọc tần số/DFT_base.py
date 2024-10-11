import numpy as np
import matplotlib.pyplot as plt
import cv2

# Định nghĩa hàm biến đổi DFT
def DFT1D(img):
    U = len(img)
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


def IDFT1D(img):
    U = len(img)
    outarry = np.zeros(U, dtype = complex)
    for n in range(U):
        sum = 0.0
        for m in range(U):
            e = np.exp(1j * 2 * np.pi * m * n / U)
            sum += img[m] * e
            print(f"accumulated sum = {sum}")
        pixel = sum / U
        outarry[n] = pixel
        print(f"DFT[{m}] = {outarry[m]}")
    return outarry