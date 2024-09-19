import numpy as np
import matplotlib.pyplot as plt

# Check if a point belongs to the Mandelbrot set


def mandelbrot(c, max_iter):
    """
    Calculate the number of iterations required to determine if a complex number 'c' belongs to the Mandelbrot set.

    Parameters:
    c (complex): The complex number to be evaluated.
    max_iter (int): The maximum number of iterations allowed to classify 'c' within the Mandelbrot set.

    Returns:
    int: The number of iterations needed to classify 'c' within the Mandelbrot set,
         or 'max_iter' if the limit is not reached.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z * z + c
    return max_iter


# Set the image size and bounds of the complex plane


width, height = 800, 800
real_min, real_max = -2.0, 1.0
imag_min, imag_max = -2.0, 2.0  # Adjust the imaginary bounds for a square aspect ratio

# Create an empty array


image = np.zeros((height, width))

# Generate the Mandelbrot set


max_iter = 256
for x in range(width):
    for y in range(height):
        # Map pixel position to a point in the complex plane
        real = real_min + (x / (width - 1)) * (real_max - real_min)
        imag = imag_min + (y / (height - 1)) * (imag_max - imag_min)
        c = complex(real, imag)

        # Determine the color of the pixel based on the number of iterations
        color = mandelbrot(c, max_iter)
        image[y, x] = color

# Plot the set


plt.imshow(image, extent=[real_min, real_max, imag_min, imag_max], cmap="inferno")
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()