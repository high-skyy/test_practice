# 토마토 창고 인접한 토마토 익음 (대각선 x) 며칠 지나면 토마토 다 익는지

# 익은 마토 -> 1 / 익지 않은 토마토 -> 0 / 토마토 x -> -1

# input 받기
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split(' '))
box = [list(map(int, sys.stdin.readline().split(' '))) for i in range(N)]

# 다 익은 것 판별 (따로 num 으로 아니면 검사) -> num

# 처음 익은 위치 찾고 -> BFS
visited = []
dq = deque()
not_ripe_num = 0
depth = 0
for row in range(N):
    for col in range(M):
        if box[row][col] == 1:
            dq.append([row, col, depth])
        if box[row][col] == 0:
            not_ripe_num += 1
d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]
if not_ripe_num == 0:
    print(0)
else:
    while dq:
        cur_row, cur_col, depth = dq.popleft()
        for i in range(4):
            new_row = cur_row + d_row[i]
            new_col = cur_col + d_col[i]
            if new_row >= N or new_row < 0 or new_col >= M or new_col < 0:
                continue
            if box[new_row][new_col] == -1 or box[new_row][new_col] == 1:
                continue
            else:
                box[new_row][new_col] = 1
                dq.append([new_row, new_col, depth+1])
                not_ripe_num -= 1
    if not_ripe_num == 0:
        print(depth)
    else:
        print(-1)