# mmcassets.py - CTCL 2024
# Purpose: Renames and copies downloaded MultiMC Minecraft assets to a new directory
# Created: December 25, 2024
# Modified: December 25, 2024
# License: The Unlicense


import os
import json
import shutil

with open("indexes/19.json") as f:
    index = json.loads(f.read())["objects"]

if not os.path.exists("out/"):
   os.mkdir("out/")

for name, data in index.items():
    assetpath = "/".join(name.split("/")[:-1])
    if not assetpath or assetpath == "/":
        continue

    if not os.path.exists(os.path.join("out/", assetpath)):
        os.makedirs(os.path.join("out/", assetpath))

    hashpath = os.path.join(data["hash"][:2], data["hash"])
    shutil.copyfile(os.path.join("objects/", hashpath), os.path.join("out/", name))
