# wav2flac.py
# Created: October 2, 2023
# Modified: March 24, 2025
# Purpose: Converts .wav files to .flac using ffmpeg

import os

# Get all files in the current directory
currentfiles = [f for f in os.listdir(".") if os.path.isfile(f)]
# Get only .wav files
currentfiles = [i for i in currentfiles if i.endswith(".wav")]

for f in currentfiles:
    print(f"Processing file: {f}")
    os.system(f"ffmpeg -i \"{f}\" -c:a flac \"{f[:-4]}.flac\"")
