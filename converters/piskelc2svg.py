# Piskel C to SVG converter - CTCL 2024
# Created: May 13, 2024
# Modified: May 13, 2024
# Purpose: Converts C array export from Piskel to SVG files made up of squares

# NOTE: Currently just supports files with one frame

from os import listdir
from os.path import isfile, join
import drawsvg as dw
import os

path = "."

filelist = [f for f in listdir(path) if isfile(join(path, f))]
filelist = [f for f in filelist if f.endswith(".c")]

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def processfile(filepath):
    with open(filepath) as f:
        content = f.readlines()

    width = int(content[3].split(" ")[2])
    height = int(content[4].split(" ")[2])

    data = "".join(content[10:]).replace("\n", "").split("}")[0].split(", ")
    # Data is exported for little-endian CPU architectures and must be "reversed"
    data = [l[2:][::-1] for l in data]

    rows = chunks(data, width)

    d = dw.Drawing(width * 10, height * 10)

    ypos = 0
    xpos = 0
    for y in rows:
        for x in y:
            color = f"#{x[:-2]}"
            opacity = int(x[-2:], 16) / 256
            if opacity > 0:
                d.append(dw.Rectangle(xpos, ypos, 10, 10, fill = color, fill_opacity = opacity))
            xpos += 10
        xpos = 0
        ypos += 10

    newfilepath = filepath[:-2] + ".svg"

    d.save_svg(newfilepath)

for filepath in filelist:
    processfile(filepath)
