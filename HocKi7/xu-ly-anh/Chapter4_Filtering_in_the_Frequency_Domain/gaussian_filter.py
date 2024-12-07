import cv2
import numpy as np

def gaussian_filter(image, kernel_size=(5, 5), sigmaX=0):
    """
    Applies a Gaussian filter to an image.

    Args:
        image: The input image.
        kernel_size: The size of the Gaussian kernel (tuple of integers).
        sigmaX: The standard deviation in the x direction (float).

    Returns:
        The filtered image.
    """

    filtered_image = cv2.GaussianBlur(image, kernel_size, sigmaX)
    return filtered_image

def gaussian_filter_2(size, size_y=None):
    size = int(size)
    if not size_y:
        size_y = size
    else:
        size_y = int(size_y)
    x, y = np.mgrid[-size:size+1, -size_y:size_y+1]
    g = np.exp(-(x**2/float(size) + y**2/float(size_y)))
    return g / g.sum()



if __name__ == "__main__":
    # Load the image
    image = cv2.imread('../images/wukong.jpg')
    
    # Apply Gaussian filtering
    filtered_image = gaussian_filter(image)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Second way
    # kernel_size = 7
    # 
    # gaussian_kernel_array = gaussian_filter_2(kernel_size)
    # 
    # # Load a generic image in grayscale (replace 'lenna.jpeg' with the actual path)
    # image = cv2.imread('you_img.jpeg', cv2.IMREAD_GRAYSCALE)
    # 
    # # Apply Gaussian filter to the image
    # filtered_image = convolve(image, gaussian_kernel_array)
    # 
    # # Display the original and filtered images
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Gaussian Filtered Image', filtered_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
        
    
