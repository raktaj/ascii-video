import numpy as np
import cv2
import sys
from filters import apply_filters

def frame_to_ascii(frame, ascii_chars, invert, edges, filter_type):
    frame = apply_filters(frame, filter_type)
    if edges:
        # Convert to grayscale if not already
        if len(frame.shape) == 3:  
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        else:
            gray = frame  # Already grayscale

        gray = cv2.Canny(frame, 100, 200)
        brightness = gray  # Use grayscale brightness directly
    else:
        # If color image, calculate perceived brightness
        if len(frame.shape) == 3:  
            brightness = (frame[:, :, 0] * 0.299 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.114).astype(np.uint8)
        else:
            brightness = frame  # Already grayscale

    # Normalize brightness to ASCII character index
    char_indices = (brightness / 255 * (len(ascii_chars) - 1)).astype(np.uint8)

    if invert:
        char_indices = len(ascii_chars) - 1 - char_indices  # Invert brightness mapping

    rows = []
    for j in range(frame.shape[0]):
        row = "".join(f"\033[38;2;{r};{g};{b}m{ascii_chars[idx]}" 
                    for (r, g, b), idx in zip(frame[j], char_indices[j]))  # Color mode

        rows.append(row)
    return rows

def render_ascii(buffer, new_frame, fps, width, height, mode):
    sys.stdout.write("\033[H")  # Move cursor to top-left

    for i, (old_row, new_row) in enumerate(zip(buffer, new_frame)):
        if old_row != new_row:
            sys.stdout.write(f"\033[{i+2};1H{new_row}")

    sys.stdout.write(f"\033[{1};{width + 8}H\033[0m FPS: {fps:.2f}  {width}x{height}  Mode: {mode}")
    sys.stdout.flush()
    
    return new_frame
