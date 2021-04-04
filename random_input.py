import os
import sys
import random
import math
from random import randrange
import glob
# FORMATO INPUT
#if 2D
#M
#radio1 property    x1   y1   (alive/dead (0/1))
#radio1 property    x2   y2   (alive/dead (0/1)) 
#radio1 property    x3   y3   (alive/dead (0/1)) 

#if 3D
#M
#radio1 property1   x1   y1     z1   (alive/dead (0/1))
#radio1 property2   x2   y2     z2   (alive/dead (0/1)) 
#radio1 property3   x3   y3     z3   (alive/dead (0/1)) 


# Get the total number of args passed
total = len(sys.argv)
if total != 5:
    print("4 argument needed, 1. 2D or 3D, 2. length of the side of the matrix in which there will be \'alive\', 3. percentage of alive particles (float), 4. qty of margin cells on the sides (ie 40)")
    quit()
if sys.argv[1] != "2D" and sys.argv[1] != "3D":
    print("3 argument needed, 1. 2D or 3D (check it has to be in CAPS_LOCK), 2.length of the side of the matrix in which there will be \'alive\' (L^2 (or L^3) = No of cells), 3. percentage of alive particles (float)")
    quit()
input_file = "input" + ".txt"
if os.path.exists(input_file):
    os.remove(input_file)
input = open(input_file, "a")

fileList = glob.glob('ovito.*d.*.xyz')
print(fileList)
for filePath in fileList:
    try:
        os.remove(filePath)
    except:
        print("Error while deleting file : ", filePath)

OPEN_SPACE = int(sys.argv[4])
L = int(sys.argv[2])
w, h, d = L+ 2*OPEN_SPACE, L +2*OPEN_SPACE, L+2*OPEN_SPACE
alive_percentage = float(sys.argv[3]) / 100

input.write(str(w))
input.write('\n')

if sys.argv[1] == "2D":
    alive_count = math.ceil(L ** 2 * alive_percentage)
    dead_count = math.floor(L ** 2 * (1 - alive_percentage))
    alive = []
    print(alive_count)
    while(len(alive) < alive_count):
        x_rand, y_rand = OPEN_SPACE+randrange(L), OPEN_SPACE+randrange(L)
        if([x_rand, y_rand] not in alive):
            alive.append([x_rand, y_rand])
    for y in range(h):
        for x in range(w):
            # radius
            input.write("0.5")
            input.write('\t')
            # property
            input.write('1')
            input.write('\t')
            # x
            input.write(str(x))
            input.write('\t')
            # y
            input.write(str(y))
            input.write('\t')
            # alive/dead
            if [x,y] in alive:
                input.write('1')
            else:
                input.write('0')
            input.write('\n')
else:
    alive_count = math.ceil(L ** 3 * alive_percentage)
    dead_count = math.floor(L ** 3 * (1 - alive_percentage))
    alive = []
    for i in range(alive_count):
        alive.append([OPEN_SPACE+randrange(L), OPEN_SPACE+randrange(L), OPEN_SPACE + randrange(L)])
    for z in range(d):
        for y in range(h):
            for x in range(w):
                # radius
                input.write("0.5")
                input.write('\t')
                # property
                input.write('1')
                input.write('\t')
                # x
                input.write(str(x))
                input.write('\t')
                # y
                input.write(str(y))
                input.write('\t')
                # z 
                input.write(str(z))
                input.write('\t')
                # alive/dead
                if [x,y,z] in alive:
                    input.write('1')
                else:
                    input.write('0')
                input.write('\n')

input.close()
