# piskelc2svg.py
# Purpose: Converts C array export from Piskel to SVG files made up of squares
# Created: May 13, 2024
# Modified: January 29, 2025

# NOTE: Currently supports files with only one frame

from os import listdir
from os.path import isfile, join
import drawsvg as dw
import os
import argparse

parser = argparse.ArgumentParser(description = "Converts C array export from Piskel to SVG files made up of squares")
parser.add_argument("-p", type = str, default = ".", help = "Path to file or directory (default .)")
parser.add_argument("-s", type = int, default = 64, help = "Size in pixels of each square (default 64)")
parser.add_argument("--union", action="store_true", help = "Use Inkscape to combine (union) all square objects into a single SVG object")
args = parser.parse_args()

path = args.p
blocksize = args.s
union = args.union

if isfile(path): 
    filelist = [path]
else:
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
    data = [pix[2:] for pix in data]
    # Data is exported for little-endian CPU architectures
    tmp = []
    for pix in data:
        ba = bytearray.fromhex(pix)
        ba.reverse()
        tmp.append(ba.hex())
    data = tmp

    rows = chunks(data, width)

    d = dw.Drawing(width * blocksize, height * blocksize)

    ypos = 0
    xpos = 0
    for y in rows:
        for x in y:
            color = f"#{x[:-2]}"
            opacity = int(x[-2:], 16) / 256
            if opacity > 0:
                d.append(dw.Rectangle(xpos, ypos, blocksize, blocksize, fill = color, fill_opacity = opacity))
            xpos += blocksize
        xpos = 0
        ypos += blocksize

    newfilepath = filepath[:-2] + ".svg"

    d.save_svg(newfilepath)

    if union: 
        os.system(f"inkscape --export-type=svg --export-plain-svg --export-overwrite -g --batch-process {newfilepath} --verb='EditSelectAll;SelectionUnion;FileSave'")

for filepath in filelist:
    processfile(filepath)
