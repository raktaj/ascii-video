# Live ASCII Video in Python

This program captures live video from your webcam and converts each frame into ASCII art, optionally using RGB color or grayscale mode. The result is displayed in your terminal, with live updates to simulate a video feed in ASCII format.

---

## ✨ Features

* Converts live webcam video into colorful or grayscale ASCII art.
* Toggle between **color mode** and **grayscale mode** with the `t` key.
* **Screenshot feature** – press `s` to save the current ASCII frame as a `.txt` file.
* Displays the current **frames per second (FPS)** in real time.
* Adjusts the aspect ratio for better viewing.
* Uses ANSI escape codes to display RGB colors in the terminal.
* Optimized with a static terminal buffer to prevent flickering.
* Simple keyboard controls:

  * `q`: Quit the program
  * `t`: Toggle color/grayscale mode
  * `s`: Save screenshot

---

## 🧰 Prerequisites

* Python 3.x
* OpenCV (`cv2`)
* NumPy
* `keyboard` module

Install with:

```bash
pip install opencv-python numpy keyboard
```

---

## 🚀 How to Run

1. Ensure your webcam is connected and functioning.
2. Run the Python script:

```bash
python ascii_video.py
```

3. View the live ASCII video in your terminal.
4. Use the hotkeys to interact:

   * `q`: Quit
   * `t`: Toggle grayscale mode
   * `s`: Save a screenshot as `ascii_screenshot_<timestamp>.txt`

---

## ⚙️ How It Works

* **Frame Capture**: Uses OpenCV to capture frames from your webcam.
* **Frame Resizing**: Resizes each frame for faster processing and maintains aspect ratio.
* **Brightness Mapping**: Converts each pixel’s brightness into a corresponding ASCII character.
* **Color Handling**: Supports both full RGB ANSI coloring and grayscale modes.
* **Static Buffer**: Prevents flickering by reusing terminal space with ANSI cursor movements.
* **FPS Calculation**: Tracks and displays real-time FPS using a frame timing buffer.
* **Screenshot Saving**: Writes the current ASCII frame to a `.txt` file with timestamp.

---

## 📁 Code Structure

* `resize_frame(frame, new_width=80)`: Resizes the video frame.
* `frame_to_ascii(frame, use_color=True)`: Converts a video frame to colored or grayscale ASCII.
* `render_ascii(ascii_art)`: Renders ASCII art efficiently to the terminal.
* `calculate_fps()`: Calculates and updates real-time FPS display.
* `save_ascii_screenshot(ascii_art)`: Saves the current frame as a `.txt` file.
* `live_ascii_video()`: Main loop to run the live ASCII video display.

---

## 🎛️ Customization

* **Frame Width**: Change `new_width` in `resize_frame()` to resize ASCII output.
* **ASCII Characters**: Customize the `ASCII_CHARS` string for different visual styles.
* **Grayscale Toggle**: Default is color; toggle with the `t` key.
* **FPS Display**: Toggle display logic or update interval in `calculate_fps()` if needed.

---

## ⚠️ Known Limitations

* Requires a terminal that supports ANSI escape codes.
* Performance varies based on system resources and webcam quality.
* Keyboard hotkeys may not work properly on some systems without administrator access (especially on Linux for the `keyboard` module).

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute it with attribution.

---

Would you like me to generate the corresponding `LICENSE` file too?
