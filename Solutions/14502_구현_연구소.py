# 연구소 N*M
# 꼭 벽 3개 생성
# 안전 영역 최댓 값

import sys
from itertools import combinations
from collections import deque

N,M = map(int, sys.stdin.readline().split(' '))
board = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split(' ')))
    board.append(temp)
"""
for line in board:
    print(line)
"""
space_list = []
virus_loc = []
wall_loc = []
for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            space_list.append((row, col))
        elif board[row][col] == 1:
            wall_loc.append((row, col))
        else:
            virus_loc.append((row, col))

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]
max_value = -1
for comb in combinations(space_list, 3):
    for row, col in comb:           # 새로운 벽 생성
        board[row][col] = 1
    count = len(space_list) - 3
    visited = [loc for loc in virus_loc]
    dq = deque()
    for loc in visited:
        dq.append(loc)
    while dq:
        cur_row, cur_col = dq.popleft()
        for i in range(4):
            new_row = cur_row + d_row[i]
            new_col = cur_col + d_col[i]
            if new_row >= N or new_row < 0 or new_col >= M or new_col < 0:
                continue
            if board[new_row][new_col] == 0:
                if (new_row, new_col) not in visited:
                    visited.append((new_row, new_col))
                    dq.append((new_row, new_col))
                    count -= 1
        if max_value != -1:
            if count < max_value:
                break
    if count > max_value:
        max_value = count
    for row, col in comb:
        board[row][col] = 0
print(max_value)


# 벽의 경우의 수 -> combination
# 2 퍼지게 만들고 -> 갯수 세기 -> max_value