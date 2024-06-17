# BDF to pixel art TTF font - CTCL 2024
# Created: June 17, 2024
# Modified: June 17, 2024
# Purpose: Converts BDF format fonts into vector TTF fonts with glyphs made up of squares

# Warning: The following code is a total hack and may be unreadable

from bdfparser import Font
from os import listdir
from os.path import isfile, join
import drawsvg as dw
import os
import argparse
import sys
import os.path
import json
import fontforge

IMPORT_OPTIONS = ('removeoverlap', 'correctdir')

infile = "./Pixel-18x18-condensed-24.bdf"

kerning_pix = 3

# TODO: Add a way to specify font file in command line
bdffont = Font(infile)
glyphs = bdffont.glyphs

svgglyphs = {}
for x, y in glyphs.items():
    glyph = bdffont.glyphbycp(y[1])

    glyph_width = glyph.meta["bbw"]
    glyph_height = int(bdffont.props["pixel_size"])

    if glyph_width > 1:
        glyphrep = str(glyph.draw().crop(glyph.meta["bbw"], glyph_height, glyph.meta["bbxoff"], glyph.meta["bbyoff"]))
    
        rows = glyphrep.split("\n")
    
        d = dw.Drawing(glyph.meta["bbw"] * 64, glyph_height * 64)
    
        ypos = (64 * abs(y[5]))
        print(ypos)
        xpos = 0
        for row in rows:
            for pix in row:
                if pix == "#":
                    d.append(dw.Rectangle(xpos, ypos, 64, 64, fill = "#000000", fill_opacity = 255))
                xpos += 64
            xpos = 0
            ypos += 64
    
        newfilepath = y[0] + ".svg"
    
        if not os.path.exists(newfilepath):
            d.save_svg(newfilepath)

            os.system(f"inkscape --export-type=svg --export-plain-svg --export-overwrite -g --batch-process {newfilepath} --verb='EditSelectAll;SelectionUnion;FileSave'")

        svgglyphs[y[1]] = {"file": y[0] + ".svg", "meta": glyph.meta}

font = fontforge.font()
font.fontname = bdffont.props["font_name"]
font.familyname = bdffont.props["face_name"]
font.fullname = bdffont.headers["fontname"]
font.ascent = 64 * int(bdffont.props["font_ascent"])
font.descent = 64 * int(bdffont.props["font_descent"])

for cp, data in svgglyphs.items():
    g = font.createMappedChar(cp)
    g.importOutlines(data["file"], IMPORT_OPTIONS)
    g.width = 64 * (int(data["meta"]["bbw"]) + kerning_pix)
    g.removeOverlap()

font.generate(infile[:-3] + "ttf")
