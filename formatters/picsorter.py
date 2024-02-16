# picsorter.py - CTCL 2023-2024
# Purpose: Sorts pictures into directories based on file name
# Created: October 17, 2023
# Modified: February 16, 2024
# License: CC0

# WARNING: This script may cause data loss in some cases, use at your own risk. 
# The "name" option is for Android devices that use the P_YYYYMMDD_HHMMSS or V_YYYYMMDD_HHMMSS format such as the ASUS Zenfone 9 running Android 13 that I use.
# The "meta" option is for Apple devices that have date information in the file's EXIF/metadata.

import os, shutil, sys
from os import listdir
from os.path import isfile, join
from PIL import Image, ExifTags

def get_date_taken(path):
    try:
        exif = Image.open(path)._getexif()
    except:
        print(f"Unknown errror when processing {path}")
        return None

    if not exif:
        return None
        print(f"{path} does not have metadata")
    try:
        return exif[36867][:10]
    except KeyError:
        print(f"{path} does not have date metadata")
        return None

mypath = "."

# Get all file names
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

months = {
    "01": "jan",
    "02": "feb",
    "03": "mar",
    "04": "apr",
    "05": "may",
    "06": "jun",
    "07": "jul",
    "08": "aug",
    "09": "sep",
    "10": "oct",
    "11": "nov",
    "12": "dec"
}

args = sys.argv
# Check how many arguments
if len(args) > 2:
    print(f"WARNING: Arguments after {sys.argv[1]} ignored")
elif len(args) < 2:
    print("ERROR: Not enough arguments")
    print("Usage: picsorter.py <name|meta>")
    sys.exit()

if args[1] == "name":
    # Make sure only images or video are in the list
    tmplst = []
    for name in onlyfiles:
        if (name.endswith(".jpg") or name.endswith(".png") or name.endswith(".mp4")) and (name.startswith("P_") or name.startswith("V_")):
            tmplst.append(name)

    onlyfiles = tmplst

    # Get the dates from the file names
    dates = []
    for name in onlyfiles:
        name = name[2:10]
        if name not in dates:
            dates.append(name)

    dirdicts = []
    for date in dates:
        dirdicts.append({date: f"{months[date[4:6]]}_{date[6:8]}_{date[:4]}"})

    for dirname in dirdicts:
        dirname = list(dirname.values())[0]
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print(f"Directory {dirname} already exists.")
            pass

    for name in onlyfiles:
        for dirdict in dirdicts:
            for key, value in dirdict.items():
                if name[2:10] == key:
                    shutil.move(name, f"{value}/{name}")
elif args[1] == "meta":
    try:
        os.mkdir("nometa/")
    except FileExistsError:
        pass

    tmplst = []
    for name in onlyfiles:
        if name.endswith(".JPG") or name.endswith(".PNG"):
            tmplst.append(name)
    onlyfiles = tmplst

    dates = []
    for name in onlyfiles:
        date = get_date_taken(name)

        if date != None:
            if date not in dates:
                dates.append(date)
    
    dirdicts = []
    for date in dates:
        splitdate = date.split(":")
        dirdicts.append({date: f"{months[splitdate[1]]}_{splitdate[2]}_{splitdate[0]}"})

    for dirname in dirdicts:
        dirname = list(dirname.values())[0]
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print(f"Directory {dirname} already exists.")
            pass

    for name in onlyfiles:
        if get_date_taken(name) == None:
            shutil.move(name, f"nometa/{name}")
        else:
            for dirdict in dirdicts:
                for key, value in dirdict.items():
                    if os.path.exists(name):
                        if get_date_taken(name) == key:
                            shutil.move(name, f"{value}/{name}")


