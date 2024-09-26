# BDF to pixel TTF font - CTCL 2024
# Created: June 17, 2024
# Modified: September 22, 2024
# Purpose: Converts BDF format fonts into vector TTF fonts with glyphs made up of squares

# Warning: The following code is a total hack and may be unreadable
# Warning 2: Currently, this script only works on Linux or other UNIX-like systems with /dev/shm 

from bdfparser import Font
import drawsvg as dw
import os
import sys
import fontforge
import argparse

parser = argparse.ArgumentParser(description = "Converts BDF files to SVG files")
parser.add_argument(type = str, help = "Path to file", required = True)
# Overrides value in BDF file
parser.add_argument(type = str, "-f", "--family-name", required = False)
# Overrides value in BDF file
parser.add_argument(type = str, "-t", "--font-type", help = "Font type, e.g. \"Bold\", \"Normal\"", required = False)
args = parser.parse_args()

infile = args.p

bdffont = Font(infile)
glyphs = bdffont.glyphs

svgglyphs = {}
for x, y in glyphs.items():
    glyph = bdffont.glyphbycp(y[1])

    glyph_width = glyph.meta["dwx0"]
    glyph_height = int(bdffont.props["pixel_size"])

    if glyph_width > 1:
        #glyphrep = str(glyph.draw().crop(glyph.meta["bbw"], glyph_height, glyph.meta["bbxoff"], 0))
   
        rows = []
        for i in range((glyph_height - glyph.meta["bbh"]) - int(bdffont.props["font_descent"]) - glyph.meta["bbyoff"]):
            rows.append("0" * glyph.meta["dwx0"])       

        for datarow in glyph.meta["hexdata"]:
            if datarow == "00":
                rows.append("0" * glyph.meta["dwx0"])
            else:
                rows.append(("0" * glyph.meta["bbxoff"]) + str(bin(int(datarow, 16))[2:]).rjust(len(datarow) * 4, "0"))

        d = dw.Drawing(glyph.meta["dwx0"] * 64, glyph_height * 64)
        ypos = 0
        xpos = 0
        isempty = True
        for row in rows:
            for pix in row:
                if pix == "1":
                    isempty = False
                    d.append(dw.Rectangle(xpos, ypos, 64, 64, fill = "#000000", fill_opacity = 255))
                xpos += 64
            xpos = 0
            ypos += 64
    
        newfilepath = "/dev/shm/" + y[0] + ".svg"
        
        d.save_svg(newfilepath)

        

        svgglyphs[y[1]] = {"file": newfilepath, "meta": glyph.meta, "isempty": isempty}

font = fontforge.font()
font.encoding = "UnicodeFull"


try:
    font.fontname = bdffont.props["font_name"]
except:
    font.fontname = infile[:-3]

try:
    font.familyname = bdffont.props["face_name"]
except:
    font.familyname = infile[:-3]

try:
    font.fullname = bdffont.headers["fontname"]
except:
    font.fullname = infile[:-3]

font.ascent = 64 * int(bdffont.props["font_ascent"])
font.descent = 64 * int(bdffont.props["font_descent"])

for cp, data in svgglyphs.items():
    g = font.createMappedChar(cp)
    if not data["isempty"]:
        g.importOutlines(data["file"], ('removeoverlap', 'correctdir'))
    g.width = 64 * (int(data["meta"]["dwx0"]))
    g.removeOverlap()

#for cp, data in svgglyphs.items():
#    os.remove(data["file"])

font.generate(infile[:-3] + "ttf")
