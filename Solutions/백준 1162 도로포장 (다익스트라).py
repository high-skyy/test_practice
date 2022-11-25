# K개의 도로 포장 도로는 이미 있는 도로만 포장 가능
# 포장 되면 시간이 0
# 서울 -> 1번 도시 / 포천 -> N번 도시

import sys
import heapq
from collections import defaultdict
from collections import deque

num_city, num_road, K = map(int, sys.stdin.readline().strip().split(' '))

road_dict = defaultdict(list)
INF = float('inf')
for _ in range(num_road):
    start, end, length = map(int, sys.stdin.readline().strip().split(' '))
    road_dict[start].append([end, length])
    road_dict[end].append([start, length])

# find_every_possible_path
starting_point = 1
end_point = num_city
result = [ [INF] * (K+1) for _ in range(num_city + 1) ]
num_k_used = 0
q = [(0, 1, 0)]
for i in range(K+1):
    result[1][i] = 0

while q:
    tot_length, cur, k_used = heapq.heappop(q)
    if cur == end_point:
        print(tot_length)
        break
    for end, length in road_dict[cur]:
        if tot_length + length < result[end][k_used]:
            heapq.heappush(q, (tot_length + length, end, k_used))
            result[end][k_used] = tot_length + length
        if k_used < K:
            if tot_length < result[end][k_used + 1]:
                heapq.heappush(q, (tot_length, end, k_used + 1))
                result[end][k_used+1] = tot_length
