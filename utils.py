import cv2
import time
import datetime

# Resize camera frame
def resize_frame(frame, new_width=100):
    height, width = frame.shape[:2]
    new_height = int(height / width * new_width * 0.55)
    return cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# Calculate FPS
def calculate_fps(prev_time):
    start_time = time.time()
    frame_time = start_time - prev_time
    fps = 1 / frame_time if frame_time > 0 else 30  # Prevent division by zero
    return fps, start_time

# Captures Video
def capture_video():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open camera.")
    return cap