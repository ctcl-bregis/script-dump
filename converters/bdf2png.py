# bdf2png.py
# Created: March 18, 2025
# Modififed: April 28, 2025
# Purpose: Generates a character map image from a BDF font file

import sys
import argparse
import math
import json
from bdfparser import Font
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser(description = "Converts BDF files to SVG files")
parser.add_argument("input", type = str, help = "Path to file")
parser.add_argument("output", type = str, help = "Output path")
parser.add_argument("json", type = str, help = "JSON map output path")
args = parser.parse_args()

infile = args.input
outfile = args.output

bdffont = Font(infile)

glyphsperrow = 64

glyphs = bdffont.glyphs

glyphx = bdffont.headers["fbbx"]
glyphy = bdffont.headers["fbby"]

imgx = glyphx * glyphsperrow
imgy = glyphy * (math.ceil(len(glyphs) / glyphsperrow) + 1)

img = Image.new(mode = "RGBA", size = (imgx, imgy), color = (0,0,0,0))


glyphmap = {}
glyphnum = 0
for name, data in glyphs.items():
    glyphnum += 1
    glyph = bdffont.glyphbycp(data[1])

    glyph_width = glyph.meta["dwx0"]
    glyph_height = glyphy

    if glyph_width > 1:
        rows = []
        for i in range((glyph_height - glyph.meta["bbh"]) - int(bdffont.props["font_descent"])):
            rows.append("0" * glyph.meta["dwx0"])

        for datarow in glyph.meta["hexdata"]:
            if datarow == "00":
                rows.append("0" * glyph.meta["dwx0"])
            else:
                rows.append(("0" * glyph.meta["bbxoff"]) + str(bin(int(datarow, 16))[2:]).rjust(len(datarow) * 4, "0"))
    else:
        continue

    glim = Image.new("RGBA", (glyph.meta["dwx0"], glyph_height), (0,0,0,0))
    gldw = ImageDraw.Draw(glim)

    pixarray = []
    for y in range(glyph_height):
        for x in range(glyphx):
            if rows[y][x] == "1":
                pixarray.append((x,y))

    gldw.point(pixarray, fill = (255,255,255,255))
    py = (math.ceil(glyphnum / glyphsperrow)) * glyphy
    px = (glyphnum - ((glyphnum // glyphsperrow) * glyphsperrow)) * glyphx

    glyphpos = (px, py)

    glyphmap[name] = {
        "startx": px,
        "starty": py,
        "endx": px + glyphx,
        "endy": py + glyphy
    }

    img.paste(glim, glyphpos)


with open(args.json, "w") as f:
    json.dump(glyphmap, f, indent = 4)

img.save(outfile)




