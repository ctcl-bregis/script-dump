# SVG Path Union - CTCL 2024
# Created: May 13, 2024
# Modified: May 13, 2024
# Purpose: Combines SVG shapes into a single SVG object

from os import listdir
from os.path import isfile, join

path = "."

filelist = [f for f in listdir(path) if isfile(join(path, f))]
filelist = [f for f in filelist if f.endswith(".svg")]

for filepath in filelist:
    os.system(f"inkscape --export-type=svg --export-plain-svg -g --batch-process {filepath} --verb='EditSelectAll;SelectionUnion;FileSave'")
