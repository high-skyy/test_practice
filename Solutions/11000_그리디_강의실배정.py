# N 개의 수업 S시작 T 끝남 -> 최소 강의실 수

import sys
import heapq
N = int(sys.stdin.readline())
S_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
room = []
S_list.sort()
heapq.heappush(room,S_list[0][1])         # 가장 작은 end_time
for i in range(1,N):
    if S_list[i][0] < room[0]:
        heapq.heappush(room,S_list[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,S_list[i][1])
print(len(room))