import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images
image_path1 = 'cap.jpg.jpg'
image_path2 = ''
img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)

# Convert images to grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Calculate histograms
hist_img1 = cv2.calcHist([gray_img1], [0], None, [256], [0, 256])
hist_img2 = cv2.calcHist([gray_img2], [0], None, [256], [0, 256])

# Normalize histograms for better visualization
hist_img1 = hist_img1 / hist_img1.sum()
hist_img2 = hist_img2 / hist_img2.sum()

# Calculate histogram correlation
hist_correlation = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
print(f"Histogram Correlation: {hist_correlation}")

# Plot histograms
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(hist_img1)
plt.title('Histogram of Image 1')

plt.subplot(1, 2, 2)
plt.plot(hist_img2)
plt.title('Histogram of Image 2')

plt.tight_layout()
plt.show()
