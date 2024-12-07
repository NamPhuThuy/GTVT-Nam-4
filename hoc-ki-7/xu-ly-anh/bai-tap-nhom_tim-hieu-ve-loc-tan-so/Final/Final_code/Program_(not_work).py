import matplotlib.pyplot as plt
import cv2
from Filters import *
from DFT_base import *

# Load the image
img = np.asarray(cv2.imread('../image/lenna_2.png', 0))  # Assuming grayscale

cv2.imwrite("../Code_demo/1_original_image.png", img)

# Perform 2D Fourier Transform
dft = dft_2d(img)

# Shift the zero-frequency component to the center
dft_shift = fft_shift(dft)


# Calculate the magnitude spectrum
magnitude_spectrum = 20 * np.log10(my_abs(dft_shift))
print(magnitude_spectrum)
cv2.imwrite("../Code_demo/2_spectrum.png", magnitude_spectrum)


rows, cols = img.shape
filter = gen_gaussian_high_pass_filter(10, rows, cols)
cv2.imwrite("../Code_demo/3_filter.png", filter)

applied_filter_image = filter * magnitude_spectrum

cv2.imwrite("../Code_demo/4_filtered_image.png", applied_filter_image)

restructed_image = idft_2d(applied_filter_image)
cv2.imwrite("../Code_demo/5_reconstructed_image.png", restructed_image)

# Create a figure and subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
# Flatten the axes array for easier indexing
# axes = axes.flatten()

axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('1. Original Image')
axes[0, 0].axis('off')

axes[0, 1].imshow(magnitude_spectrum, cmap='gray')
axes[0, 1].set_title('2. Spectrum')
axes[0, 1].axis('off')

axes[0, 2].imshow(filter, cmap='gray')
axes[0, 2].set_title('3. Filter')
axes[0, 2].axis('off')

axes[1, 0].imshow(applied_filter_image, cmap='gray')
axes[1, 0].set_title('4. Filtered Image')
axes[1, 0].axis('off')

axes[1, 1].imshow(restructed_image, cmap='gray')
axes[1, 1].set_title('5. Reconstructed Image')
axes[1, 1].axis('off')

# axes[1, 2].imshow(img6, cmap='gray')
# axes[1, 2].set_title('Image 6')
# axes[1, 2].axis('off')

plt.tight_layout()
plt.savefig("../result")
plt.show()