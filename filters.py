import cv2
import numpy as np

def apply_filters(frame, filter_type):
    if filter_type == "sepia":
        sepia_filter = np.array([[0.393, 0.769, 0.189],
                                 [0.349, 0.686, 0.168],
                                 [0.272, 0.534, 0.131]])
        frame = frame.astype(np.float32)
        frame = np.dot(frame, sepia_filter.T)
        frame = np.clip(frame, 0, 255).astype(np.uint8)

    elif filter_type == "negative":
        frame = 255 - frame

    elif filter_type == "pixelated":
        small = cv2.resize(frame, (20, 15), interpolation=cv2.INTER_LINEAR)
        frame = cv2.resize(small, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)

    elif filter_type == "grayscale":
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)  # keep 3-channel format

    elif filter_type == "scanlines":
        frame = frame.copy()
        frame[::2] = (frame[::2] * 0.5).astype(np.uint8)

    elif filter_type == "posterize":
        levels = 6
        factor = 256 // levels
        frame = ((frame // factor) * factor).astype(np.uint8)
    elif filter_type == "soft":
        # Apply a light Gaussian blur
        frame = cv2.GaussianBlur(frame, (5, 5), sigmaX=1)

        # Reduce contrast slightly
        frame = cv2.convertScaleAbs(frame, alpha=1.1, beta=15)

        # Slight desaturation to soften colors
        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV).astype(np.float32)
        hsv[...,1] *= 0.6  # Reduce saturation
        hsv[...,1] = np.clip(hsv[...,1], 0, 255)
        frame = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)

    return frame

def apply_mode_instructions(frame, mode_instructions):
    """Applies all filters and effects defined in a rendering mode."""
    for instruction in mode_instructions:
        if instruction in {"sepia", "negative", "pixelated", "soft", "posterize", "scanlines", "grayscale"}:
            frame = apply_filters(frame, instruction)
    return frame
