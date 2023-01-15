# 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수
'''
주의
1. 다시 0 으로 돌아올 필요는 없다.
2. 한번에 M권 들 수 있다.
'''

import sys
import heapq
N, M = map(int, sys.stdin.readline().split(' '))
book_loc_list = list(map(int, sys.stdin.readline().split(' ')))
left_list = []
right_list = []
for loc in book_loc_list:
    if loc < 0:
        heapq.heappush(left_list, loc)
    else:
        heapq.heappush(right_list, -loc)
cur = 0
tot_distance = 0
max_distance = 0
last_max_distance = 0
while left_list:
    distance = heapq.heappop(left_list)
    if max_distance < -distance:
        max_distance = -distance
    cur += 1
    if cur == M:
        last_max_distance = max(last_max_distance, max_distance)
        tot_distance += max_distance * 2
        max_distance = 0
        cur = 0
if cur != 0:
    last_max_distance = max(last_max_distance, max_distance)
    tot_distance += max_distance * 2
    max_distance = 0
    cur = 0
while right_list:
    distance = heapq.heappop(right_list)
    if max_distance < -distance:
        max_distance = - distance
    cur += 1
    if cur == M:
        last_max_distance = max(last_max_distance, max_distance)
        tot_distance += max_distance * 2
        max_distance = 0
        cur = 0
if cur != 0:
    last_max_distance = max(last_max_distance, max_distance)
    tot_distance += max_distance * 2
    max_distance = 0
    cur = 0
print(tot_distance - last_max_distance)

