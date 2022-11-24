# 통학버스 한대(정원)

from collections import defaultdict
import heapq

# get input
apart_num, bus_cap, school_loc = map(int,input().split(' '))
student_loc = defaultdict(int)
for _ in range(apart_num):
    loc, num = map(int,input().split(' '))
    student_loc[loc] = num

left_q = []
right_q = []
for loc in student_loc:
    if loc > school_loc:
        heapq.heappush(right_q, (- abs(loc - school_loc), student_loc[loc]))
    if loc < school_loc:
        heapq.heappush(left_q, (-abs(loc - school_loc), student_loc[loc]))
# print(left_q, right_q)

total_distance = 0
num_in_bus = 0
max_dist = 0
for q in [left_q, right_q]:
    while q:
        dist, num = heapq.heappop(q)
        num_in_bus += num
        max_dist = max(-dist, max_dist)
        if num_in_bus > bus_cap:
            remain = num_in_bus - bus_cap
            total_distance += max_dist * 2
            max_dist, num_in_bus = 0, 0
            heapq.heappush(q, (dist, remain))

    if num_in_bus != 0:
        total_distance += max_dist * 2
        max_dist, num_in_bus = 0, 0
print(total_distance)
