# draw.io connection point style generator - CTCL 2024
# Purpose: Creates list of connection points for each side of a rectangle
# Created: July 18, 2024
# Modifeid: July 18, 2024

# Right = 1,0,0,0,x
# Left = 0,0,0,0,x
# Top = 0,0,0,x,0
# Bottom = 0,1,0,x,0

# size = [width, height]
size = [360, 200];
grid = 10;

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
