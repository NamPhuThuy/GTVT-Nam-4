import cv2
import numpy as np

def calculate_mse(image1, image2):
    """Calculates the Mean Squared Error (MSE) between two images.
  
    Args:
        image1: The first image.
        image2: The second image.
  
    Returns:
        The calculated MSE value.
    """

    # Ensure both images have the same shape
    if image1.shape != image2.shape:
        raise ValueError("Images must have the same shape.")

    # Calculate the squared difference between corresponding pixels
    squared_diff = np.square(image1 - image2)

    # Calculate the mean of the squared differences
    mse = np.mean(squared_diff)

    return mse

def calculate_snr(original_image, noisy_image):
    """Calculates the Signal-to-Noise Ratio (SNR) between two images.
  
    Args:
        original_image: The original image.
        noisy_image: The noisy image.
  
    Returns: 
  
        The calculated SNR value in decibels (dB).
    """

    mse = calculate_mse(original_image, noisy_image)
    snr = 10 * np.log10(np.mean(original_image**2) / mse)

    return snr


# Load images
original_image = cv2.imread('original_image.jpg')
noisy_image = cv2.imread('noisy_image.jpg')

# Calculate MSE and SNR
mse_value = calculate_mse(original_image, noisy_image)
snr_value = calculate_snr(original_image, noisy_image)

print("MSE:", mse_value)
print("SNR:", snr_value, "dB")