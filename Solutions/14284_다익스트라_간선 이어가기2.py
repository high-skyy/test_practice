# 정점 n개, 0개의 -> 무방향
# s->t 연결 -> 간선 추가 멈춘다.
'''
주의
1. 간선의 가중치의 합이 최소가 되도록 함
2. output : 최솟 값
'''

import sys
from collections import defaultdict
import heapq
n, m = map(int, sys.stdin.readline().split(' '))
path_dict = defaultdict(list)
for _ in range(m):
    start, end, value = map(int, sys.stdin.readline().split(' '))
    path_dict[start].append([end, value])
s, t = map(int, sys.stdin.readline().split(' '))

q = []
heapq.heappush(q, (0, start))
INF = m*100 + 1
value_list = [INF for _ in range(n+1)]
value_list[s] = 0
while q:
    cur_val, cur_loc = heapq.heappop(q)
    if value_list[cur_loc] < cur_val:
        continue
    for dest, value in path_dict[cur_loc]:
        if value_list[dest] > value + cur_val:
            value_list[dest] = value + cur_val
            heapq.heappush(q, (value + cur_val, dest))
# 모든 간선 저장 -> 다익스트라 -> 그 자체 거리가 정답
print(value_list[t])