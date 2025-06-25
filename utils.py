import cv2
import time
import shutil

# Resize camera frame with aspect ratio correction for ASCII output
def resize_frame(frame, target_cols=None, target_rows=None, correction_factor=0.5):
    if target_cols is None or target_rows is None:
        term_cols, term_rows = get_terminal_size_in_chars()
        target_cols = term_cols
        target_rows = term_rows

    height, width = frame.shape[:2]
    aspect_ratio = width / height

    # Adjust height to account for character aspect ratio
    new_width = target_cols
    new_height = int((target_cols / aspect_ratio) * correction_factor)

    # Ensure it fits within terminal dimensions
    if new_height > target_rows:
        new_height = target_rows
        new_width = int((target_rows / correction_factor) * aspect_ratio)

    resized = cv2.resize(frame, (new_width, new_height))
    return resized

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

def get_terminal_size_in_chars():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.columns, size.lines
