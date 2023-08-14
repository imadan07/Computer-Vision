import cv2
import numpy as np

# Load the image
image_path = 'cap.jpg.jpg'
img = cv2.imread(image_path)

# Define animation parameters
num_frames = 30  # Number of frames in the animation
animation_speed = 30  # Animation speed in frames per second

# Get the dimensions of the image
height, width, _ = img.shape

# Create a VideoWriter object to save the animation
output_path = 'output_animation.gif'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, animation_speed, (width, height))

# Create the animation by modifying the image frames
for i in range(num_frames):
    # Rotate the image slightly for each frame
    angle = 360 * (i / num_frames)
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_frame = cv2.warpAffine(img, rotation_matrix, (width, height))

    out.write(rotated_frame)

# Release the VideoWriter object
out.release()

print(f'Animation saved as {output_path}')
