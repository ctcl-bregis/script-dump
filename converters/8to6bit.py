# 8to6bit.py
# Purpose: Converts 8-bit values to 6-bit values
# Created: September 15, 2024
# Modified: January 29, 2025

# Formulas from: https://threadlocalmutex.com/?p=48

import argparse

parser = argparse.ArgumentParser(prog = "8to6bit", description = "Converts 8-bit values to 6-bit values")
parser.add_argument("input", type = str)
parser.add_argument("-t", "--type", choices = ["dec", "hex", "rgb"])

args = parser.parse_args()

x = args.input

# This script is for calculating the displayed equivalent RGB888 color on an RGB666 display being driven from an RGB888 interface where bits of each color on the RGB666 display is connected to bits 2-7 (out of 0-7) of each color channel on the RGB888 interface.
# Basically, the first two bits of each 8-bit color value are ignored

if args.type == "dec":
    x = int(args.input)
    x &=~ (1<<0)
    x &=~ (1<<1)
    print(x)
elif args.type == "hex": 
    x = int(args.input, 16)
    x &=~ (1<<0)
    x &=~ (1<<1)
    print(x)
elif args.type == "rgb":
    x = [int(args.input[i:i+2], 16) for i in range(0, len(args.input), 2)]
    x = [i &~ (1<<1) for i in x] 
    x = [i &~ (1<<0) for i in x] 
    x = [hex(i)[2:].ljust(2, "0") for i in x]
    print("".join(x))
   
