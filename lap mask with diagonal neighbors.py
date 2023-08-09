import cv2
import numpy as np
image_path = 'spidy.png.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
laplacian_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])
sharpened_image = cv2.filter2D(image, cv2.CV_8U, laplacian_kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image (Extended Laplacian)', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
