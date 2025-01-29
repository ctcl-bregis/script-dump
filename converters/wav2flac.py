# wav2flac.py
# Created: October 2, 2023
# Modified: January 29, 2025
# Purpose: Converts .wav files to .flac

from pydub import AudioSegment
from os import listdir
from os.path import isfile, join

# Get all files in the current directory
currentfiles = [f for f in listdir(".") if isfile(join(".", f))]
# Get only .wav files
currentfiles = [i for i in currentfiles if i.endswith(".wav")]

for f in currentfiles:
    print(f"Processing file: {f}")
    track = AudioSegment.from_wav(f)
    track.export(f.replace(".wav", ".flac"), format = "flac")
