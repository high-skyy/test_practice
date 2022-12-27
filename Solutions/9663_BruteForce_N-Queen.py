# N-Queen 문제

import sys
from itertools import combinations


N = int(sys.stdin.readline())
loc_list = [[row, col] for row in range(N) for col in range(N)]

count = 0
for comb in combinations(loc_list, N):
    vertical_list = []
    horizontal_list = []
    y_x = []
    y_x_reverse = []
    possible = True
    for row, col in comb:
        if row in horizontal_list:
            possible = False
            break
        if col in vertical_list:
            possible = False
            break
        if row + col in y_x:
            possible = False
            break
        if col - row in y_x_reverse:
            possible = False
            break
        horizontal_list.append(row)
        vertical_list.append(col)
        y_x.append(row + col)
        y_x_reverse.append(col - row)
    if possible:
        count += 1
print(count)
