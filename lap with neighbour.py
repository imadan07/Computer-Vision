import cv2
import numpy as np

# Load the image
image_path = 'spidy.png.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the Laplacian kernel with extension to diagonal neighbors
laplacian_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply the custom Laplacian kernel
sharpened_image = cv2.filter2D(image, cv2.CV_8U, laplacian_kernel)

# Display the original image and the sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image (Extended Laplacian)', sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
