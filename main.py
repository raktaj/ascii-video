import cv2
import time
import keyboard
from settings import get_args, ASCII_CHAR_SETS
from ascii_renderer import frame_to_ascii, render_ascii
from utils import capture_video, resize_frame, calculate_fps

def live_ascii_video():
    args = get_args()
    cap = capture_video()
    greyscale_mode = False
    ASCII_CHARS = ASCII_CHAR_SETS[args.asciichars]

    try:
        print("\033[2J\033[H", end="")  # Clear screen once at the start
        _, frame = cap.read()
        frame = resize_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        buffer = frame_to_ascii(frame, ASCII_CHARS, args.invert, args.edges, args.filter, greyscale_mode)

        prev_time = time.time()
        fps = 30  # Prevent ZeroDivisionError

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = resize_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            new_frame = frame_to_ascii(frame, ASCII_CHARS, args.invert, args.edges, args.filter, greyscale_mode)

            fps, prev_time = calculate_fps(prev_time)

            height, width = frame.shape[:2]
            mode = "Edge Detection" if args.edges else "Greyscale" if greyscale_mode else "Color"

            buffer = render_ascii(buffer, new_frame, fps, width, height, mode)

            if keyboard.is_pressed("q"):
                break
            if keyboard.is_pressed("t"):  
                greyscale_mode = not greyscale_mode  # Toggle mode
                time.sleep(0.2)  # Prevent rapid toggling
    finally:
        print("\033[0m\033[2J")
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    live_ascii_video()
