# D킬로미터 길이의 고속도로
# 지름길 -> 일방통행행

import sys
import heapq
from collections import defaultdict
N, D = map(int, sys.stdin.readline().split(' '))
sc_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
sc_list = sorted(sc_list, lambda x : x[0])
value_list = [i for i in range(D + 1)]
for  in sc_list:

