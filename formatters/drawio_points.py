# drawio_points.py
# Purpose: Creates list of connection points for each side of a rectangle
# Created: July 18, 2024
# Modified: May 26, 2025
import argparse

parser = argparse.ArgumentParser(description = "Creates list of connection points for each side of a rectangle for use in draw.io")
parser.add_argument("w", metavar = "W", type = int, help = "Width")
parser.add_argument("h", metavar = "H", type = int, help = "Height")
parser.add_argument("g", metavar = "G", type = int, default = 10, help = "Grid")
args = parser.parse_args()

# Right = 1,0,0,0,x
# Left = 0,0,0,0,x
# Top = 0,0,0,x,0
# Bottom = 0,1,0,x,0

# size = [width, height]
size = [args.w,args.h]
grid = args.g

right = []
left = []
top = []
bottom = []

for i in range(1, size[0] // grid):
    top.append([0,0,0,i * grid,0])
    bottom.append([0,1,0,i * grid,0])

for i in range(1, size[1] // grid):
    right.append([1,0,0,0,i * grid])
    left.append([0,0,0,0,i * grid])

points = []
points += right
points += left
points += top
points += bottom

print(repr(points).replace(" ", ""))
