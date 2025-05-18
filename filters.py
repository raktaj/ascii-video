import cv2
import numpy as np

def apply_filters(frame, filter_type):
    if filter_type == "sepia":
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                 [0.349, 0.686, 0.168],
                                 [0.272, 0.534, 0.131]])
        frame = frame.astype(np.float32)  # Convert to float for matrix multiplication
        frame = np.dot(frame, sepia_filter.T)  # Apply sepia filter
        frame = np.clip(frame, 0, 255).astype(np.uint8)  # Keep pixel values in range

    elif filter_type == "negative":
        frame = 255 - frame  # Invert colors

    elif filter_type == "pixelated":
        small = cv2.resize(frame, (20, 15), interpolation=cv2.INTER_LINEAR)
        frame = cv2.resize(small, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

    return frame
