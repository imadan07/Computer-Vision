import cv2
import numpy as np
image_path = 'spidy.png.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
laplacian_kernel = np.array([
    [ 0,  1,  0],
    [ 1, -4,  1],
    [ 0,  1,  0]
])
opened_image = cv2.filter2D(blurred_image, cv2.CV_64F, laplacian_kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Opened Image (Positive Laplacian)', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
