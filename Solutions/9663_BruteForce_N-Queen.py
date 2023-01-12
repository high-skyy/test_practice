# N-Queen 문제

import sys
from itertools import permutations

# row + col // col - row
N = int(sys.stdin.readline())
queen_list = [-1 for i in range(N)]
global count

def nqueen(cur_index):
    global count
    if cur_index == n:
        count += 1
