# Live ASCII Video in Python

This program captures live video from your webcam and converts each frame into colorful ASCII art. The result is displayed in your terminal, with live updates to simulate a video feed in ASCII format.

## Features

- Converts live webcam video into colorful ASCII art.
- Adjusts the aspect ratio for better viewing.
- Uses ANSI escape codes to display RGB colors in the terminal.
- Optimized with a static terminal buffer to prevent flickering.
- Press `q` to quit the program.

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- NumPy
- Keyboard

## Installation

1. Clone this repository or download the `ascii_video.py` file.
2. Install the required libraries:

    ```bash
    pip install opencv-python numpy keyboard
    ```

## How to Run

1. Ensure your webcam is connected and working.
2. Run the Python script:

    ```bash
    python ascii_video.py
    ```

3. The live video will be displayed as ASCII art in your terminal.
4. Press `q` to exit the program.

## How It Works

1. **Frame Capture**: The program captures frames from your webcam using OpenCV.
2. **Frame Resizing**: The frames are resized for faster processing and to maintain an appropriate aspect ratio for ASCII display.
3. **Brightness Calculation**: For each pixel, the program calculates the brightness and selects a corresponding ASCII character based on the brightness level.
4. **Color Mapping**: The program maps the RGB values of each pixel to ANSI escape codes, allowing the ASCII characters to retain the original colors of the video.
5. **Static Buffer Rendering**: Instead of clearing the screen each frame, the program moves the cursor to the top-left to prevent terminal flickering and provide a smoother experience.

## Code Structure

- **`resize_frame(frame, new_width=80)`**: Resizes the video frame while maintaining the aspect ratio.
- **`frame_to_ascii(frame)`**: Converts a video frame into an ASCII art string, with RGB colors applied.
- **`render_ascii(ascii_art)`**: Efficiently writes ASCII art to the terminal using a static buffer approach.
- **`live_ascii_video()`**: Main function that captures video, converts it to ASCII art, and displays it in the terminal.

## Customization

- **Frame Width**: You can adjust the width of the ASCII video by modifying the `new_width` parameter in the `resize_frame` function.
- **ASCII Characters**: You can change the characters used for different brightness levels by modifying the `ASCII_CHARS` string.

## Known Limitations

- This program is designed to run in terminals that support ANSI escape codes. Some terminals may not fully support colored output.
- Performance may vary based on system capabilities and the webcam's frame rate.

## License

This project is licensed under the MIT License. Feel free to use and modify it.
