import argparse

# ASCII character sets
ASCII_CHAR_SETS = {
    "classic": "Ñ@#W$9876543210?!abc;:+=-,._",
    "blocks": "█▓▒░ ",
    "minimal": "@%#*+=-:. "
}

def get_args():
    parser = argparse.ArgumentParser(description="Live ASCII Video")
    parser.add_argument("-a", "--asciichars", choices=ASCII_CHAR_SETS.keys(), default="classic",
                        help=f"Choose an ASCII character set")
    parser.add_argument("-i", "--invert", action="store_true",
                        help="Invert ASCII brightness for light terminals")
    parser.add_argument("-e", "--edges", action="store_true",
                        help="Enable edge detection (sketch effect)")
    parser.add_argument("-f", "--filter", choices=["sepia", "negative", "pixelated"], default=None,
                        help="Apply a filter before ASCII conversion")

    return parser.parse_args()
