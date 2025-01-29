# logo.py
# Purpose: Generates single-letter logos
# Created: December 29, 2024
# Modified: January 29, 2025

import argparse

parser = argparse.ArgumentParser(
    prog = "logo",
    description = "Generate a logo"
)
parser.add_argument("character")
parser.add_argument("bgcolor")
parser.add_argument("fgcolor")
args = parser.parse_args()

characters = {
    "C": "M4 2H12V4H6V12H12V14H4Z",
    "I": "M4 2H12V4H9V12H12V14H4V12H7V4H4Z",
    "L": "M4 2V14H12V12H6V2Z",
    "M": "M4 2H6V3H7V4H9V3H10V2H12V14H10V6H9V7H7V6H6V14H4Z",
    "S": "M4 2V9H10V12H4V14H12V7H6V4H12V2Z",
    "T": "M4 2H12V4H9V14H7V4H4Z"
}

character = characters.get(args.character)
if character is None:
    print(f"Character not implemented or invalid: {args.character}")
    exit(1)
bgcolor = args.bgcolor
fgcolor = args.fgcolor

output = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <rect width="16" height="16" fill="{bgcolor}" />
    <path d="{character}" fill="{fgcolor}" />
</svg>
""".format(bgcolor = bgcolor, fgcolor = fgcolor, character = character)

with open(f"out.svg", "w") as f:
    f.write(output)