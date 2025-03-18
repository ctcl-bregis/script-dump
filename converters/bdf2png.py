import sys
import argparse
import math
from bdfparser import Font
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser(description = "Converts BDF files to SVG files")
parser.add_argument("p", type = str, help = "Path to file")
parser.add_argument("o", type = str, help = "Output path")
args = parser.parse_args()

infile = args.p

bdffont = Font(infile)

glyphsperrow = 64

glyphs = bdffont.glyphs

glyphx = bdffont.headers["fbbx"]
glyphy = bdffont.headers["fbby"]

imgx = glyphx * glyphsperrow
imgy = glyphy * (math.ceil(len(glyphs) / glyphsperrow) + 1)

img = Image.new(mode = "RGBA", size = (imgx, imgy), color = (0,0,0,0))

glyphnum = 0
for name, data in glyphs.items():
    glyphnum += 1
    glyph = bdffont.glyphbycp(data[1])

    glyph_width = glyph.meta["dwx0"]
    glyph_height = int(bdffont.props["pixel_size"])

    if glyph_width > 1:
        rows = []
        for i in range((glyph_height - glyph.meta["bbh"]) - int(bdffont.props["font_descent"]) - glyph.meta["bbyoff"]):
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
    for y in range(glyph_height - 1):
        for x in range(glyph.meta["dwx0"] - 1):
            if rows[y][x] == "1":
                pixarray.append((x,y))

    gldw.point(pixarray, fill = (255,255,255,255))
    py = (math.ceil(glyphnum / glyphsperrow)) * glyphy
    px = (glyphnum - ((glyphnum // glyphsperrow) * glyphsperrow)) * glyphx

    print(px)

    glyphpos = (px, py)
    img.paste(glim, glyphpos)

img.show()




