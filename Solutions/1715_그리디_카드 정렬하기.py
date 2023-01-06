# A 묶음 B 묶음 비교 -> A+B 번 필요하다

import sys
import heapq


N = int(sys.stdin.readline().rstrip())
num_list = []
for _ in range(N):
    heapq.heappush(num_list, int(sys.stdin.readline()))

# 가장 작은 것 먼저 합친다. -> 최소 (그리디?)
total_result = 0
while len(num_list) >= 2:
    cur_1 = heapq.heappop(num_list)
    cur_2 = heapq.heappop(num_list)
    total_result = total_result + cur_1 + cur_2
    heapq.heappush(num_list, cur_1 + cur_2)
print(total_result)