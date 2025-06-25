import cv2
import time
import keyboard
from settings import get_args, ASCII_CHAR_SETS, RENDER_MODES
from ascii_renderer import frame_to_ascii, render_ascii
from utils import capture_video, resize_frame, calculate_fps
from filters import apply_filters, apply_mode_instructions

def live_ascii_video():
    args = get_args()
    cap = capture_video()

    ASCII_CHARS = ASCII_CHAR_SETS[args.asciichars]
    mode_instructions = RENDER_MODES.get(args.mode, [])

    try:
        print("\033[2J\033[H", end="")  # Clear screen once at the start

        _, frame = cap.read()
        frame = resize_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Apply rendering mode filters if any
        if mode_instructions:
            frame = apply_mode_instructions(frame, mode_instructions)
        elif args.filter:
            frame = apply_filters(frame, args.filter)

        buffer = frame_to_ascii(
            frame,
            ASCII_CHARS,
            invert=args.invert or "invert" in mode_instructions,
            edges=args.edges or "edges" in mode_instructions,
            filter_type=args.filter
        )

        prev_time = time.time()
        fps = 30  # Prevent ZeroDivisionError on first frame

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = resize_frame(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            if mode_instructions:
                frame = apply_mode_instructions(frame, mode_instructions)
            elif args.filter:
                frame = apply_filters(frame, args.filter)

            new_frame = frame_to_ascii(
                frame,
                ASCII_CHARS,
                invert=args.invert or "invert" in mode_instructions,
                edges=args.edges or "edges" in mode_instructions,
                filter_type=args.filter
            )

            fps, prev_time = calculate_fps(prev_time)
            height, width = frame.shape[:2]

            mode = args.mode if args.mode else ("Edge Detection" if args.edges else "Color")
            buffer = render_ascii(buffer, new_frame, fps, width, height, mode)

            if keyboard.is_pressed("q"):
                break

    finally:
        print("\033[0m\033[2J")  # Reset formatting and clear screen
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    live_ascii_video()
