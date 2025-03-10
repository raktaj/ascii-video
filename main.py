import cv2
import numpy as np
import sys
import keyboard

# ASCII characters based on brightness levels
ASCII_CHARS = "Ñ@#W$9876543210?!abc;:+=-,._"

# Resize the frame
def resize_frame(frame, new_width=100):
    height, width = frame.shape[:2]
    new_height = int(height / width * new_width * 0.55)  # Maintain aspect ratio
    return cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# Convert frame to ASCII
def frame_to_ascii(frame):
    # Use perceptual luminance formula for brightness
    brightness = (frame[:, :, 0] * 0.299 + frame[:, :, 1] * 0.587 + frame[:, :, 2] * 0.114).astype(np.uint8)
    char_indices = (brightness / 255 * (len(ASCII_CHARS) - 1)).astype(np.uint8)

    rows = []
    for j in range(frame.shape[0]):
        row = "".join(f"\033[38;2;{r};{g};{b}m{ASCII_CHARS[idx]}" 
                      for (r, g, b), idx in zip(frame[j], char_indices[j]))
        rows.append(row)

    return rows  # Returns a list of rows

# Optimized rendering using a static buffer
def render_ascii(buffer, new_frame):
    for i, (old_row, new_row) in enumerate(zip(buffer, new_frame)):
        if old_row != new_row:  # Only update changed lines
            sys.stdout.write(f"\033[{i+1};1H{new_row}")  # Move to line `i+1` and update
    sys.stdout.flush()
    return new_frame  # Update buffer

# Main function to capture live video and display ASCII
def live_ascii_video():
    cap = cv2.VideoCapture(0)
    try:
        print("\033[2J", end="")  # Clear screen once at start
        _, frame = cap.read()
        frame = resize_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        buffer = frame_to_ascii(frame)  # Initialize buffer

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = resize_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            new_frame = frame_to_ascii(frame)

            buffer = render_ascii(buffer, new_frame)  # Only update necessary parts

            if keyboard.is_pressed("q"):
                break
    finally:
        print("\033[0m")
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    live_ascii_video()
