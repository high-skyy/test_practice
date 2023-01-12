# 트리의 node 사이의 경로 중 가장 긴 경로의 길이

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
INF = 100 * (N-1) + 1
FW = [[INF for i in range(N+1)] for j in range(N+1)]

for i in range(N-1):
    parent, child, weight = map(int, sys.stdin.readline().rstrip().split(' '))
    FW[parent][child] = weight
    FW[child][parent] = weight

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                continue
            FW[i][j] = min(FW[i][j] , FW[i][k] + FW[k][j])

max_val = 0
for i in range(N):
    for j in range(N):
        if FW[i][j] == INF:
            continue
        else:
            if FW[i][j] > max_val:
                max_val = FW[i][j]

print(max_val)
for line in FW:
    print(line)

