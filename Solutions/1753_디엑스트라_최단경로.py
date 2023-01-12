# 시작점에서 다음 정점으로 최단 경로 (가중치 10 이하)
'''
주의
1. 여러개의 간선
2. vertice는 1부터 시작
3. 경로 존재 x -> INF  출력
4. output : start 에서 끝에 가는데 값 출력
'''
# FW 알고
# input 받기
import sys
from collections import defaultdict
import heapq

V, E = map(int, sys.stdin.readline().rstrip().split(' '))
start = int(sys.stdin.readline())
path_dict = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split(' '))
    path_dict[u].append([v,w])
'''
주의
1. 여러개의 간선
2. vertice는 1부터 시작
3. 경로 존재 x -> INF  출력
4. output : start 에서 끝에 가는데 값 출력 -> 디엑스트라
'''
# 초기화
q = [[0, start]]
INF = E * 10 + 1
value_list = [INF for _ in range(V+1)]
value_list[start] = 0
while q:
    cur_val , cur_loc = heapq.heappop(q)
    if cur_val > value_list[cur_loc]:
        continue
    for dest, value in path_dict[cur_loc]:
        if value_list[dest] > value + cur_val:
            value_list[dest] = value + cur_val
            heapq.heappush(q, [value + cur_val, dest])
for i in range(1, V+1):
    if value_list[i] == INF:
        print('INF')
    else:
        print(value_list[i])


