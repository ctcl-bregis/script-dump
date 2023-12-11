# picsorter.py - CTCL 2023
# Purpose: Sorts pictures into directories based on file name
# Date: October 17, 2023 - December 11, 2023
# License: CC0

# WARNING: This script may cause data loss in some cases, use at your own risk. This script was made for Android devices that use the P_YYYYMMDD_HHMMSS or V_YYYYMMDD_HHMMSS format such as the ASUS Zenfone 9 running Android 12 that I use.

import os, shutil
from os import listdir
from os.path import isfile, join

mypath = "."

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

# Get all file names
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Make sure only images or video are in the list
tmplst = []
for name in onlyfiles:
    if name.endswith(".jpg") or name.endswith(".png") or name.endswith(".mp4"):
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
