# 다익스트라

# 방향성 x 인 그래프에서 1번 정범에서 N번 정점 최단 거리
# 주어진 두 정점은 반드시 거치면서 가는 경로의 수

import sys
from collections import defaultdict
import heapq

N, E = map(int, sys.stdin.readline().rstrip().split(' '))

path_dict = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    path_dict[a-1].append([b-1,c])
    path_dict[b-1].append([a-1,c])

v1, v2 = map(int, sys.stdin.readline().rstrip().split(' '))
v1 -= 1
v2 -= 1
INF = (N-1)*200000 + 1
dy_start = [INF for i in range(N)]
dy_start[0] = 0
dy_v1 = [INF for i in range(N)]
dy_v1[v1] = 0
dy_v2 = [INF for i in range(N)]
dy_v2[v2] = 0
end = N-1

for dy, start in zip([dy_start, dy_v1, dy_v2], [0, v1, v2]):
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cost, cur = heapq.heappop(q)
        for next, add_cost in path_dict[cur]:
            new_cost = cost + add_cost
            if dy[next] >= new_cost:
                dy[next] = new_cost
                heapq.heappush(q, [new_cost, next])

answer = min(dy_start[v1] +dy_v1[v2] + dy_v2[end], dy_start[v2] + dy_v2[v1] + dy_v1[end])
if answer >= INF:
    print(-1)
else:
    print(answer)
