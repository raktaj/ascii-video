import cv2
import numpy as np
import sys

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

    # Generate ASCII art with colors
    rows = []
    for j in range(frame.shape[0]):
        row = "".join(f"\033[38;2;{r};{g};{b}m{ASCII_CHARS[idx]}" 
                      for (r, g, b), idx in zip(frame[j], char_indices[j]))
        rows.append(row)

    return "\n".join(rows) + "\033[0m"  # Reset color at the end

# Optimized console rendering using cursor positioning
def move_cursor_top():
    sys.stdout.write("\033[H")  # Move cursor to the top-left corner
    sys.stdout.flush()

# Main function to capture live video and display ASCII
def live_ascii_video():
    cap = cv2.VideoCapture(0)  # Capture video from webcam
    try:
        print("\033[2J", end="")  # Clear the screen once at the beginning
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
            resized_frame = resize_frame(frame)  # Resize for faster processing
            ascii_art = frame_to_ascii(resized_frame)  # Convert frame to ASCII

            move_cursor_top()  # Move cursor to the top instead of clearing the screen
            sys.stdout.write(ascii_art + "\n")
            sys.stdout.flush()

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    live_ascii_video()
