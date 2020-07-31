import math
import sys

print("Шахматный слон ходит по диагонали")
coord = []
coord.append(int(input("x1=")))
coord.append(int(input("y1=")))
coord.append(int(input("x2=")))
coord.append(int(input("y2=")))

max_n = max(coord)
if (max_n > 9):
    sys.exit()
if (math.fabs(coord[0] - coord[2]) == math.fabs(coord[1] - coord[3])):
    print("Yes")
else:
    print("No")
