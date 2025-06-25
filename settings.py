import argparse
import os
import json


# Load rendering options from JSON
def load_rendering_options():
    path = os.path.join(os.path.dirname(__file__), "rendering_options.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

RENDERING_OPTIONS = load_rendering_options()
ASCII_CHAR_SETS = RENDERING_OPTIONS["ascii_char_sets"]
RENDER_MODES = RENDERING_OPTIONS.get("modes", {})

def get_args():
    parser = argparse.ArgumentParser(
        description="Live ASCII Video Renderer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    general = parser.add_argument_group("General Options")
    general.add_argument("-a", "--asciichars", choices=ASCII_CHAR_SETS.keys(), default="classic",
                         help="Choose an ASCII character set")
    general.add_argument("-i", "--invert", action="store_true",
                         help="Invert ASCII brightness for light terminals")

    modes = parser.add_argument_group("Rendering Modes")
    modes.add_argument("-e", "--edges", action="store_true",
                       help="Enable edge detection (sketch effect)")
    modes.add_argument("-m", "--mode", choices=RENDER_MODES.keys(), 
                       help="Apply a custom rendering mode") 

    filters = parser.add_argument_group("Filter Options")
    filters.add_argument("-f", "--filter", choices=["sepia", "negative", "pixelated", "grayscale", "soft", "scanlines", "posterize"],
                         default=None,
                         help="Apply a visual filter to the video")

    return parser.parse_args()
