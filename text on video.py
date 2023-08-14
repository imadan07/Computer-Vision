import cv2

# Load the video
video_path = 'yt1s.com - The Fruit Friends Song  ChuChu TV Baby Nursery Rhymes and Kids Songs.mp4'
cap = cv2.VideoCapture(video_path)

# Get the frames per second (fps) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the font and text properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 255, 255)  # White color
thickness = 2

# Loop through the frames of the video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add text overlay to the frame
    text = f'Frame Number: {int(cap.get(cv2.CAP_PROP_POS_FRAMES))}'
    cv2.putText(frame, text, (50, 50), font, font_scale, font_color, thickness, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Video with Text Overlay', frame)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
