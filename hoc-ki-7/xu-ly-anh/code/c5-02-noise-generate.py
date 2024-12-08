import cv2
import numpy as np
from utils import show_image

def generate_gaussian_noise(image, mean=0, stddev=25):
    """
    Generates Gaussian noise and adds it to the image.

    Args:
        image: The input image.
        mean: The mean of the Gaussian distribution.
        stddev: The standard deviation of the Gaussian distribution.

    Returns:
        The noisy image.
    """

    noise = np.random.normal(mean, stddev, image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def generate_salt_and_pepper_noise(image, density=0.05):
    """
    Generates salt-and-pepper noise and adds it to the image.

    Args:
        image: The input image.
        density: The density of noise (proportion of pixels to be corrupted).

    Returns:
        The noisy image.
    """

    noisy_image = image.copy()
    height, width = image.shape[:2]
    num_noise_pixels = int(density * height * width)

    for _ in range(num_noise_pixels):
        x, y = np.random.randint(0, height), np.random.randint(0, width)
        noisy_image[x, y] = np.random.randint(0, 256)

    return noisy_image

def generate_poisson_noise(image):
    """
    Generates Poisson noise and adds it to the image.

    Args:
        image: The input image.

    Returns:
        The noisy image.
    """

    noisy_image = np.random.poisson(image)
    return noisy_image

def generate_speckle_noise(image, var=0.01):
    """
    Generates speckle noise and adds it to the image.

    Args:
        image: The input image.
        var: The variance of the speckle noise.

    Returns:
        The noisy image.
    """

    noise = np.random.randn(*image.shape) * np.sqrt(var)
    noisy_image = image + image * noise
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def generate_impulse_noise(image, noise_density):
    """
    Generates impulse noise (salt-and-pepper noise) on an image.
  
    Args:
        image: The input image.
        noise_density: The proportion of pixels to be corrupted with noise.
  
    Returns:
        The noisy image.
    """

    # Create a noise mask with random values between 0 and 1
    noise_mask = np.random.rand(*image.shape)

    # Set pixels to 0 (black) or 255 (white) based on the noise mask and noise density
    noisy_image = image.copy()
    noisy_image[noise_mask < noise_density] = 0
    noisy_image[noise_mask >= noise_density] = 255

    return noisy_image
    

if __name__ == "__main__":
    # Load an image
    image = cv2.imread('../images/gray_wukong.jpg')

    # Generate Gaussian noise and add it to the image
    gaussian_noise_image = generate_gaussian_noise(image)
    salt_and_pepper_noise_image = generate_salt_and_pepper_noise(image)
    poisson_noise_image = generate_poisson_noise(image)
    speckle_noise_image = generate_speckle_noise(image)
    impulse_noise_image = generate_impulse_noise(image, 0.05)

    image_BGR_list = [gaussian_noise_image, salt_and_pepper_noise_image, poisson_noise_image, speckle_noise_image, impulse_noise_image]
    title_list = ["gaussian", "salt n pepper", "poisson", "speckle", "impulse"]
    pos_list = [1, 2, 3, 4, 5]

    show_image.show_images_with_titles_and_positions(image_BGR_list, title_list, pos_list, "Noise images example", 3)
