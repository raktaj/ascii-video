# Live ASCII Video in Python

This program captures live video from your webcam and converts each frame into colorful or stylized ASCII art. The result is displayed in your terminal in real-time, with smooth updates and optional filters, grayscale mode, and screenshot saving. Designed to be efficient, customizable, and fun to experiment with.

---

## ✨ Features

- Converts webcam video into **live ASCII art** with **color** or **grayscale**.
- Uses **ANSI escape codes** to display true RGB colors in compatible terminals.
- **Keyboard controls**:
  - `q` – Quit
  - `t` – Toggle grayscale mode
  - `s` – Save screenshot
- **Screenshot saving** as `.txt` files with timestamps.
- **FPS display** and performance-optimized rendering using static buffers.
- **Rendering modes** (like `retro`, `noir`, `chill`) for one-click styling.
- **Aspect-ratio aware resizing** that adapts to terminal size.
- **Custom ASCII sets** loaded from `rendering_options.json`.

---

## 🧰 Prerequisites

- Python 3.7 or later
- Libraries:
  ```bash
  pip install opencv-python numpy keyboard
  ```

---

## 🚀 How to Run

```bash
python ascii_video.py
```

### Optional CLI Arguments:

* `-a`, `--asciichars`: Choose ASCII set (classic, blocks, minimal)
* `-f`, `--filter`: Apply a filter (sepia, negative, soft, scanlines, etc.)
* `-e`, `--edges`: Enable edge detection overlay
* `-i`, `--invert`: Invert brightness (better for light terminals)
* `-m`, `--mode`: Use a rendering mode (e.g., `retro`, `noir`, `chill`)

Example:

```bash
python ascii_video.py -m retro
```

---

## 🎨 Filters Available

* `sepia` – Warm, vintage tone
* `negative` – Inverted colors
* `soft` – Pastel-like smoothing
* `grayscale` – Remove color before conversion
* `scanlines` – Adds CRT-style lines
* `posterize` – Reduces tonal depth for artistic effect

---

## 🧪 Rendering Modes (via `rendering_options.json`)

Define reusable modes with preconfigured filters and flags:

```json
{
  "ascii_char_sets": {
    "classic": "Ñ@#W$9876543210?!abc;:+=-,._",
    "blocks": "█▓▒░ ",
    "minimal": "@%#*+=-:. "
  },
  "modes": {
    "retro": ["sepia", "scanlines", "invert"],
    "noir": ["grayscale", "edges"],
    "chill": ["soft"]
  }
}
```

Run with:

```bash
python ascii_video.py -m noir
```

---

## 🧠 How It Works

* **Frame capture**: Via OpenCV.
* **Resize logic**: Matches terminal size and ASCII proportions.
* **Filters**: Applied before conversion.
* **Brightness mapping**: Maps pixel brightness to ASCII.
* **Color rendering**: ANSI RGB escape sequences.
* **Buffer system**: Renders only changed lines for performance.
* **Input handling**: Keyboard events for interactivity.

---

## 📁 Code Structure

* `main.py`: Core application loop and argument parsing.
* `ascii_renderer.py`: Frame-to-ASCII conversion and display.
* `filters.py`: Collection of image filters.
* `utils.py`: FPS, resizing, saving, terminal size detection.
* `rendering_options.json`: Custom character sets and modes.

---

## 🔧 Customization

* Add filters in `filters.py`.
* Add more rendering modes to the JSON file.
* Change frame width, resize logic, or font scaling in `utils.py`.

---

## ⚠️ Limitations

* Requires a terminal that supports **ANSI escape codes** (color rendering).
* `keyboard` module may need admin privileges on Linux.
* May be stretched in terminals using non-square fonts.

---

## 📄 License

This project is licensed under the **MIT License**.
Free to use, modify, and distribute with attribution.
