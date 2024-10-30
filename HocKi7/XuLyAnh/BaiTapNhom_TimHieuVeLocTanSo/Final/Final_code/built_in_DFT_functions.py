import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_high_pass_filter(D0, U, V):
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
            D[u, v] = np.sqrt((u - U0)**2 + (v - V0)**2)
            H[u, v] = 1- np.exp(-D[u, v]**2 / (2 * D0**2))

    return H

# Load the image
img = cv2.imread('../image/test.png', cv2.IMREAD_GRAYSCALE)

# Perform 2D Fourier Transform
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Create the high-pass filter
D0 = 9  # Adjust the cut-off frequency as needed
rows, cols = img.shape
H = gaussian_high_pass_filter(D0, rows, cols)

# Apply the filter in the frequency domain
filtered_dft = dft_shift * H

# Shift the zero-frequency component back
filtered_dft_shift = np.fft.ifftshift(filtered_dft)

# Perform Inverse Fourier Transform
img_back = np.fft.ifft2(filtered_dft_shift)
img_back = np.abs(img_back)

# Display the original and filtered images
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), 
plt.imshow(img_back, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show() 
