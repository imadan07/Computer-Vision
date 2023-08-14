import cv2
import numpy as np

# Load the images
image_path1 = 'cap.jpg.jpg'
image_path2 = 'Helmet.jpeg'
img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

# Initialize the ORB detector
orb = cv2.ORB_create()

# Find keypoints and descriptors
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

# Initialize the BFMatcher (Brute-Force Matcher)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw top N matches
top_n_matches = 10
match_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:top_n_matches], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the matched image
cv2.imshow('Feature Matching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
