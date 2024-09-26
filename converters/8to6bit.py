# 8-bit to 6-bit Color Depth Converter - CTCL 2024
# Created: September 15, 2024
# Modified: September 15, 2024

# Formulas from: https://threadlocalmutex.com/?p=48

import argparse

parser = argparse.ArgumentParser(prog = "8to6bit", description = "Converts 8-bit values to 6-bit values")
parser.add_argument("input", type = str)
parser.add_argument("-t", "--type", choices = ["dec", "hex", "rgb"])

args = parser.parse_args()

x = args.input

if args.type == "dec":
    x = int(args.input)
    print((x * 253 + 512) >> 10)
elif args.type == "hex": 
    x = int(args.input, 16)
    print((x * 253 + 512) >> 10)
elif args.type == "rgb":
    x = [int(args.input[i:i+2], 16) for i in range(0, len(args.input), 2)]
    x = [((i * 253 + 512) >> 10) * 4 for i in x ] 
    x = [hex(i)[2:].ljust(2, "0") for i in x]
    print("".join(x))
   
