import cv2

# Load the pre-trained eye detection classifier
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the image
image_path = 'cap.jpg.jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect eyes in the image
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw red rectangles around detected eyes
for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(image, (ex, ey), (ex + ew, ey + eh), (0, 0, 0), 2)  # Red rectangle for eyes

# Display the image with rectangles
cv2.imshow('Eye Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()