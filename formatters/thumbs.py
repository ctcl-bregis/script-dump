# Sprite to Thumbnails - CTCL 2024
# Purpose: Converts sprites into thumbnails
# Created: July 22, 2024
# Modified: July 22, 2024

from PIL import Image
import os

filelist = [i for i in os.listdir("sprites") if i.endswith(".png")]

file_bl = [
    
]

if len(file_bl) > 0:
    for path in filelist:
        if path in file_bl:
            filelist.remove(path)

if not os.path.exists("thumbs"):
    os.mkdir("thumbs")
elif os.path.exists("thumbs") and not os.path.isdir("thumbs"):
    raise Exception("thumbs exists but is not a directory")

for path in filelist:
    sprite = Image.open(os.path.join("sprites", path))
    thumb = Image.new("RGB", (512,512), (0,0,0,255))

    wpercent = (512 / float(sprite.size[0]))
    hsize = int((float(sprite.size[1]) * float(wpercent)))
    sprite = sprite.resize((512, hsize), Image.Resampling.NEAREST)
    sprite.thumbnail((384, 384), Image.Resampling.NEAREST)
    thumb.paste(sprite, (64, 64))

    thumb.save(os.path.join("thumbs", f"thumb_{path}"))
